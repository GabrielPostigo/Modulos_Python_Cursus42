from typing import Any, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self):
        self._stor: list[str] = []
        self._total: int = 0

    # Abstract method that will check whether the input
    # data are appropriate for the current data processor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # Abstract method that will process the input data
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # Method that will output ingested data
    def output(self) -> tuple[int, str]:

        if not self._stor:
            raise IndexError("No data avaible in processor")

        consumed = self._total - len(self._stor)
        value = self._stor.pop(0)
        return (consumed, value)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data) -> bool:
        """Return True if data is:
            - int
            - float
            - a list of int/float.
        """
        return (isinstance(data, (int, float)) or
                (isinstance(data, list) and
                 all(isinstance(x, (int, float)) for x in data)
                 )
                )

    def ingest(self, data: Union[int, float, list[int, float]]) -> None:
        """Convert numeric data to strings and store internally."""
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._stor.append(str(item))
                self._total += 1

        # At this point data only can be a Int or a Float
        else:
            self._stor.append(str(data))
            self._total += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        """Return True if data is:
            - str
            - a list of str.
        """
        return (isinstance(data, str) or
                (isinstance(data, list) and
                 all(isinstance(x, str) for x in data)
                 )
                )

    def ingest(self, data: Union[str, list[str]]):
        if not self.validate(data):
            raise TypeError("Improper string data")
        if isinstance(data, list):
            for item in data:
                self._stor.append(str(item))
                self._total += 1

        # At this point data only can be a String
        else:
            self._stor.append(str(data))
            self._total += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data) -> bool:
        """Return True if data is
            - dict[str,str]
            - a list thereof
        """
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        if isinstance(data, list):
            return all(isinstance(item, dict) and
                       all(isinstance(k, str) and isinstance(v, str)
                           for k, v in item.items())
                       for item in data
                       )
        return False

    def ingest(self,
               data: Union[dict[str, str], list[dict[str, str]]]) -> None:
        """Convert log dicts to 'LEVEL: message' strings and store."""
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for item in data:
                log_level = item.get("log_level", "")
                log_message = item.get("log_message", "")
                self._stor.append(f"{log_level}: {log_message}")
                self._total += 1

        # At this point data only can be a Dictionary
        else:
            log_level = data.get("log_level", "")
            log_message = data.get("log_message", "")
            self._stor.append(f"{log_level}: {log_message}")
            self._total += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    num = NumericProcessor()
    txt = TextProcessor()
    log_ = LogProcessor()

    print()

    print("Testing Numeric Processor...")

    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")  # type: ignore[arg-type]
    except TypeError as e:
        print(f" Got exception: {e}")

    data_num: list[int | float] = [1, 2, 3, 4, 5]

    print(f" Processing data: {data_num}")
    num.ingest(data_num)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()  # output -> tuple[int, str]
        print(f" Numeric value {rank}: {value}")
    print()

    print("Testing Text Processor...")

    print(f" Trying to validate input '42': {txt.validate(42)}")

    data_txt = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_txt}")
    txt.ingest(data_txt)

    print(" Extracting 1 value...")
    rank, value = txt.output()
    print(f" Text value {rank}: {value}")
    print()

    print("Testing Log Processor...")

    print(f" Trying to validate input 'Hello': {log_.validate('Hello')}")

    data_log = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    print(f" Processing data: {data_log}")
    log_.ingest(data_log)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_.output()
        print(f" Log entry {rank}: {value}")
