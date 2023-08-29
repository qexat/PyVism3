#!/usr/bin/env python3
# pyright: reportUnusedCallResult = false

import argparse
import typing

from pyvism import hooks


# For match exhaustiveness garanties
_Subcommand = typing.Literal["shell", "repl", "compile", "run", None]


def parse_args() -> argparse.Namespace:
    """
    Parse the command line arguments using `argparse`.
    """

    parser_global = argparse.ArgumentParser()
    subparsers = parser_global.add_subparsers(dest="subcommand")

    # <<= Shell subcommand =>> #
    """
    Start the REPL.

    Usage:
        vism shell
    """
    parser_shell = subparsers.add_parser("shell", aliases=["repl"])

    # <<= Compilation subcommand =>> #
    """
    Compile a .vism file into bytecode.

    Usage:
        vism compile <file> [--output <output_file>] [--strict]
    """
    parser_compile = subparsers.add_parser("compile")
    parser_compile.add_argument("c_file", type=argparse.FileType("r"), metavar="FILE")
    parser_compile.add_argument(
        "--output",
        "-o",
        type=argparse.FileType("w"),
        dest="c_output",
        metavar="FILE",
        help="send the compilation result into this file",
    )
    parser_compile.add_argument(
        "--strict",
        action="store_true",
        dest="c_strict",
        help="activate strict mode (warnings become errors)",
    )

    # <<= Run subcommand =>> #
    """
    Run a .vmbc file or compile then run a .vism file.

    Usage:
        vism run <file> [--keep-bytecode]
    """
    parser_run = subparsers.add_parser("run")
    parser_run.add_argument("r_file", type=argparse.FileType("r"), metavar="file")
    parser_run.add_argument(
        "--keep-bytecode",
        action="store_true",
        dest="r_keep_bytecode",
        help="prevent from removing the intermediate bytecode file",
    )

    # <<= Global args =>> #
    """
    Global args.
    """
    parser_global.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="enable compiler's debug mode",
    )
    parser_global.add_argument(
        "--technical",
        "-t",
        action="store_true",
        help="make messages technical rather than beginner-friendly",
    )

    return parser_global.parse_args()


def main() -> int:
    args = parse_args()
    subcommand: _Subcommand = args.subcommand

    match subcommand:
        case "shell" | "repl":
            return hooks.shell(args.debug, args.technical)
        case "compile":
            return hooks.compile(
                args.debug,
                args.technical,
                args.c_file,
                args.c_output,
                args.c_strict,
            )
        case "run":
            return hooks.run(
                args.debug,
                args.debug,
                args.r_file,
                args.r_keep_bytecode,
            )
        case None:
            print("Vism xD")
            return 1
