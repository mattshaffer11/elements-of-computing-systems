"""
This module provides .asm to .hack logic.
"""

import re

from .lookup import Lookup
from . import commands


def parse(source):
    """
    Returns hack translation of a .asm file's contents.

    Parameters
    ----------
    source : str
        Contents of .asm file.

    Returns
    -------
    formatted_translations : str
    """
    translations = []
    lookup = Lookup()
    lines = _format_source(source)

    _set_labels(lines, lookup)
    for line in lines:
        translation = _translate(line, lookup)
        print(translation)
        if not translation:
            continue

        translations.append(translation)

    return _format_translations(translations)


def _format_source(source):
    """
    Returns raw sources lines as an array of commands with comments and
    whitespacing removed.

    Parameters
    ----------
    source : str
        Contents of .asm file.

    Returns
    -------
    lines : [str]
    """
    lines = []

    raw_lines = source.strip().split("\n")
    for line in raw_lines:
        line = _remove_comments(line)
        line = _remove_whitespacing(line)
        if not len(line):
            continue

        lines.append(line)

    return lines


def _format_translations(translations):
    return "\n".join(translations)


def _set_labels(lines, lookup):
    for counter, line in enumerate(lines):
        if not _get_command_type(line) == commands.L:
            continue

        name = _get_label_name(line)
        lookup.add(name, counter)


def _translate(line, lookup):
    command_type = _get_command_type(line)

    if command_type == commands.L:
        return
    elif command_type == commands.A:
        return _translate_a_command(line, lookup)
    else:
        return _translate_c_command(line)


def _translate_l_command(line, loop):
    print(line)


def _translate_a_command(line, lookup):
    name = _get_variable_name(line)

    variable = lookup.get(name)
    if variable is None:
        lookup.add(name)

    return str(variable)


def _translate_c_command(line):
    return None


def _get_command_type(line):
    if _is_l_command(line):
        return commands.L
    elif _is_a_command(line):
        return commands.A
    elif _is_c_command(line):
        return commands.C

    # TODO: FIX
    raise Exception('NO RECOGNIZED')


def _is_l_command(line):
    return line[0] == '(' and line [-1] == ')'


def _is_a_command(line):
    return line[0] == '@'


def _is_c_command(line):
    return True
    return line[0] == '(' and line [-1] == ')'


def _replace_symbols(lines):
    return lines


def _get_variable_name(line):
    return line[1:]


def _get_label_name(line):
    return re.sub('[()]', '', line)


def _remove_whitespacing(line):
    return ''.join(line.split())


def _remove_comments(line):
    return line.split('//')[0]


def _is_valid_symbol(symbol):
    return re.search(r'^[a-zA-Z$:_.][a-zA-Z0-9$:_.]*$', symbol) is not None
