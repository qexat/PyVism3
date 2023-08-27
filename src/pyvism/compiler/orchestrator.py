import dataclasses
import os
import typing

from pyvism.compiler.interface import (
    IDatabase,
    IReporter,
    IntEnum_T,
    Runnable,
)


@dataclasses.dataclass(slots=True)
class Orchestrator(typing.Generic[IntEnum_T]):
    database: IDatabase[IntEnum_T]
    reporter: IReporter

    def run(
        self,
        *runnables: Runnable[IntEnum_T],
    ) -> int:
        for component in runnables:
            component.run(self.database)
            # <check here the component's results>

        return os.EX_OK
