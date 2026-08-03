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

    # Return the number of item still stored
    def rest(self) -> int:
        return len(self._stor)

    def total_process(self) -> int:
        return self._total


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


class DataStream:
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """
            Method that allows you to register
            a new data processor to process the data stream
        """
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """
            method that will analyze each element of the list
            received as a parameter and send it to the appropriate
            registered data processor
        """
        for e in stream:
            handled: bool = False

            for proc in self._processors:

                if proc.validate(e):

                    proc.ingest(e)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element "
                      f"in stream: {e}")

    def print_processors_stats(self) -> None:
        """
            print stream statistics.
        """
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = proc.total_process()
            remaining = proc.rest()

            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    num = NumericProcessor()
    txt = TextProcessor()
    log_ = LogProcessor()
    stream = DataStream()
    print()

    print("Initialize Data Stream...")
    stream.print_processors_stats()
    print()

    print("Registering Numeric Processor")
    stream.register_processor(num)

    batch1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()
    print()

    print("Registering other data processors")
    stream.register_processor(txt)
    stream.register_processor(log_)

    print("Send the same batch again")
    stream.process_stream(batch1)
    stream.print_processors_stats()
    print()

    print("Consume some elements from the data"
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num.output()
    for _ in range(2):
        txt.output()
    log_.output()
    stream.print_processors_stats()
