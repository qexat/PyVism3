import dataclasses
import os
import typing

from pyvism.compiler.interface import IDatabase
from pyvism.compiler.interface import IReporter
from pyvism.compiler.interface import TokenType_T
from pyvism.compiler.interface import Runnable


@dataclasses.dataclass(slots=True)
class Orchestrator(typing.Generic[TokenType_T]):
    database: IDatabase[TokenType_T]
    reporter: IReporter

    def run(
        self,
        *runnables: Runnable[TokenType_T],
    ) -> int:
        for component in runnables:
            component.run(self.database)
            # <check here the component's results>

        return os.EX_OK
