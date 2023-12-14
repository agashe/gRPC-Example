from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ("id", "name", "age")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    age: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class FetchStudentsRequest(_message.Message):
    __slots__ = ("id", "query", "perPage")
    ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PERPAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    query: str
    perPage: int
    def __init__(self, id: _Optional[int] = ..., query: _Optional[str] = ..., perPage: _Optional[int] = ...) -> None: ...

class CreateStudentRequest(_message.Message):
    __slots__ = ("name", "age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class UpdateStudentRequest(_message.Message):
    __slots__ = ("id", "name", "age")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    age: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ...) -> None: ...

class DeleteStudentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class StudentsResponse(_message.Message):
    __slots__ = ("status", "message", "students")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STUDENTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    students: _containers.RepeatedCompositeFieldContainer[Student]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., students: _Optional[_Iterable[_Union[Student, _Mapping]]] = ...) -> None: ...
