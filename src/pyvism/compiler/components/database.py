import dataclasses
import typing

from pyvism.compiler.components.token import TokenType
from pyvism.compiler.interface import IDatabase
from pyvism.compiler.interface import IToken


@dataclasses.dataclass(slots=True)
class Database(IDatabase[TokenType]):
    source: typing.TextIO
    tokens: list[IToken[TokenType]] = dataclasses.field(default_factory=list)
    ast: ... = None

    # errors: list[?]
    # warnings: list[?]
