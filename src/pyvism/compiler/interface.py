from __future__ import annotations

import abc
import enum
import typing

TokenType_T = typing.TypeVar("TokenType_T", bound=enum.IntEnum)


class Runnable(typing.Protocol[TokenType_T]):
    """
    Interface for objects that can be run on a database.
    """

    @abc.abstractmethod
    def run(self, database: IDatabase[TokenType_T]) -> None:
        pass


class IToken(typing.Protocol[TokenType_T]):
    type: TokenType_T
    start: int
    end: int
    line_no: int
    lexeme: str


class IScanner(Runnable[TokenType_T], typing.Protocol[TokenType_T]):
    # Local copy of the output -- it is then sent to the database
    tokens: list[IToken[TokenType_T]] = []

    # Scanner state values
    start: int = 0
    current: int = 0
    line_no: int = 1

    # Local copy of the input
    source: str = ""

    def push_token(self, token: IToken[TokenType_T]) -> None:
        self.tokens.append(token)


class IParser(Runnable[TokenType_T], typing.Protocol[TokenType_T]):
    # Local copy of the output -- it is then sent to the database
    ast: ...

    # Parser state value
    current: int = 0

    # Local copy of the input
    tokens: list[IToken[TokenType_T]] = []


class IDiagnostic(typing.Protocol[TokenType_T]):
    component: type[Runnable[TokenType_T]]
    id: int
    summary: str


class IError(IDiagnostic[TokenType_T], typing.Protocol):
    critical: bool


class IWarning(IDiagnostic[TokenType_T], typing.Protocol):
    pass


class IDatabase(typing.Protocol[TokenType_T]):
    source: typing.TextIO
    tokens: list[IToken[TokenType_T]]
    ast: ...

    # errors: list[?]
    # warnings: list[?]


class IReporter(typing.Protocol):
    pass
