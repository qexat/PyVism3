import dataclasses
import typing

from pyvism.compiler.components.token import TokenType
from pyvism.compiler.interface import IDiagnostic, IError, IWarning, Runnable


@dataclasses.dataclass(slots=True)
class Diagnostic(IDiagnostic[TokenType]):
    component: type[Runnable[TokenType]]
    id: int
    summary: str

    line_no: int
    spos: int
    epos: int
    message: str


@dataclasses.dataclass(slots=True)
class Error(Diagnostic, IError[TokenType]):
    @classmethod
    def new(
        cls,
        component: type[Runnable[TokenType]],
        id: int,
        line_no: int,
        spos: int,
        epos: int,
    ) -> typing.Self:
        cls()


@dataclasses.dataclass(slots=True)
class Warning(Diagnostic, IWarning[TokenType]):
    pass
