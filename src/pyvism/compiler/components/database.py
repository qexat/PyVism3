# pyright: reportIncompatibleVariableOverride = false

import dataclasses
import typing

from pyvism.compiler.components.diagnostic import Error
from pyvism.compiler.components.diagnostic import Warning
from pyvism.compiler.components.token import TokenType
from pyvism.compiler.interface import IDatabase
from pyvism.compiler.interface import IToken


@dataclasses.dataclass(slots=True)
class Database(IDatabase[TokenType]):
    source: typing.TextIO
    tokens: list[IToken[TokenType]] = dataclasses.field(default_factory=list)
    ast: ... = None

    errors: list[Error] = dataclasses.field(default_factory=list)
    warnings: list[Warning] = dataclasses.field(default_factory=list)
