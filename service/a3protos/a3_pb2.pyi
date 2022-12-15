from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishYear", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ART: Book.Genre
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    BIOGRAPHY: Book.Genre
    Business: Book.Genre
    FICTION: Book.Genre
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHYEAR_FIELD_NUMBER: _ClassVar[int]
    SCIENCE: Book.Genre
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.Genre
    publishYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., publishYear: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["Book", "number", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    Book: Book
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    number: int
    status: InventoryItem.Status
    def __init__(self, number: _Optional[int] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ..., Book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...
