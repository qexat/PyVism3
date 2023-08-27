from __future__ import annotations

import abc
import enum
import typing

IntEnum_T = typing.TypeVar("IntEnum_T", bound=enum.IntEnum)


class Runnable(typing.Protocol[IntEnum_T]):
    """
    Interface for objects that can be run on a database.
    """

    @abc.abstractmethod
    def run(self, database: IDatabase[IntEnum_T]) -> None:
        pass


class IToken(typing.Protocol[IntEnum_T]):
    type: IntEnum_T
    start: int
    end: int
    line_no: int
    lexeme: str


class IScanner(Runnable[IntEnum_T], typing.Protocol[IntEnum_T]):
    # Local copy of the output -- it is then sent to the database
    tokens: list[IToken[IntEnum_T]] = []

    # Scanner state values
    start: int = 0
    current: int = 0
    line_no: int = 1

    # Local copy of the input
    source: str = ""

    def push_token(self, token: IToken[IntEnum_T]) -> None:
        self.tokens.append(token)


class IParser(Runnable[IntEnum_T], typing.Protocol[IntEnum_T]):
    # Local copy of the output -- it is then sent to the database
    ast: ...

    # Parser state value
    current: int = 0

    # Local copy of the input
    tokens: list[IToken[IntEnum_T]] = []


class IDiagnostic(typing.Protocol[IntEnum_T]):
    component: type[Runnable[IntEnum_T]]
    id: int
    summary: str


class IError(typing.Protocol[IntEnum_T]):
    component: type[Runnable[IntEnum_T]]


class IDatabase(typing.Protocol[IntEnum_T]):
    source: typing.TextIO
    tokens: list[IToken[IntEnum_T]]
    ast: ...

    # errors: list[?]
    # warnings: list[?]


class IReporter(typing.Protocol):
    pass
