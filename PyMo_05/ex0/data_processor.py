from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

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
        pass


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    data = DataProcessor()
    num = NumericProcessor()
    txt = TextProcessor()
    print("Testing Numeric Processor...")

    print()
    print("Testing Text Processor...")

    print()
    print("Testing Log Processor...")
