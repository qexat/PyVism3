import typing

from pyvism.compiler.components.database import Database
from pyvism.compiler.components.parser import Parser
from pyvism.compiler.components.reporter import Reporter
from pyvism.compiler.components.scanner import Scanner
from pyvism.compiler.orchestrator import Orchestrator


def shell(
    debug: bool,
    technical: bool,
) -> int:
    pass


def compile(
    debug: bool,
    technical: bool,
    file: typing.TextIO,
    output: typing.TextIO | None,
    strict: bool,
) -> int:
    database = Database(file)
    reporter = Reporter()
    orchestrator = Orchestrator(database, reporter)

    scanner = Scanner()
    parser = Parser(None)

    return orchestrator.run(scanner, parser)


def run(
    debug: bool,
    technical: bool,
    file: typing.TextIO,
    keep_bytecode: bool,
) -> int:
    pass
