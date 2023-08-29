import dataclasses

from pyvism.compiler.components.token import TokenType
from pyvism.compiler.interface import IDiagnostic, IError, IWarning, Runnable


@dataclasses.dataclass(slots=True)
class Diagnostic(IDiagnostic[TokenType]):
    component: type[Runnable[TokenType]]
    id: int
    summary: str


@dataclasses.dataclass(slots=True)
class Error(Diagnostic, IError[TokenType]):
    critical: bool


@dataclasses.dataclass(slots=True)
class Warning(Diagnostic, IWarning[TokenType]):
    pass
