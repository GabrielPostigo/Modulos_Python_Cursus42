from typing import Any
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
        consumed = self._total - len(self._storage)
        value = self._storage.pop(0)
        return (consumed, value)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data) -> bool:
        return (isinstance(data, (int, float)) or
                isinstance(data, list) and
                all(isinstance(x, (int, float)) for x in data))

    def ingest(self, data) -> None:
        pass


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self) -> bool:
        return isinstance(data, dict)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    data = DataProcessor()
    num = NumericProcessor()
    txt = TextProcessor()
    print()

    print("Testing Numeric Processor...")

    print()

    print("Testing Text Processor...")

    print()

    print("Testing Log Processor...")
