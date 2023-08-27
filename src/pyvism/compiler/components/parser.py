# pyright: reportImplicitOverride = false

import dataclasses
from pyvism.compiler.components.token import TokenType

from pyvism.compiler.interface import IDatabase, IParser


@dataclasses.dataclass(slots=True)
class Parser(IParser[TokenType]):
    ast: ...

    def run(self, database: IDatabase[TokenType]) -> None:
        ...
