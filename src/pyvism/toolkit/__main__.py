#!/usr/bin/env python3

import shutil


INTRO = " PyVism ToolKit "


def main() -> None:
    width, _ = shutil.get_terminal_size()

    print(INTRO.center(width, "─"))
