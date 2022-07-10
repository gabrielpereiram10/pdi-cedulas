from typing import Any


class Image:

    def __init__(self, filename: str, file: Any, note: int) -> None:
        self.filename = filename
        self.file = file
        self.note = note

    def __repr__(self) -> str:
        return self.filename
