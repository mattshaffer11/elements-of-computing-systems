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
    """
    Returns array of translated .hack commands as a single str.

    Parameters
    ----------
    translations : [str]

    Returns
    -------
    result : str
    """
    return "\n".join(translations)


def _set_labels(lines, lookup):
    """
    Adds labels to symbol lookup table.

    Parameters
    ----------
    lines : [str]
    lookup : Lookup
    """
    for counter, line in enumerate(lines):
        if not _get_command_type(line) == commands.L:
            continue

        name = _get_label_name(line)
        lookup.add(name, counter)


def _translate(line, lookup):
    """
    Translates a single line.

    Parameters
    ----------
    line : str
    lookup : Lookup

    Returns
    -------
    translated_line : str
    """
    command_type = _get_command_type(line)

    if command_type == commands.L:
        return
    elif command_type == commands.A:
        return _translate_a_command(line, lookup)
    else:
        return _translate_c_command(line)


def _translate_a_command(line, lookup):
    """
    Translates an A command.

    Parameters
    ----------
    line : str
    lookup : Lookup

    Returns
    -------
    translated_line : str
    """
    name = _get_variable_name(line)

    variable = lookup.get(name)
    if variable is None:
        lookup.add(name)

    return str(variable)


def _translate_c_command(line):
    """
    Translates a C command.

    Parameters
    ----------
    line : str
    lookup : Lookup

    Returns
    -------
    translated_line : str
    """
    return None


def _get_command_type(line):
    """
    Determines the type of command from a line.

    Parameters
    ----------
    line : str

    Returns
    -------
    command_type : str
    """
    if _is_l_command(line):
        return commands.L
    elif _is_a_command(line):
        return commands.A
    elif _is_c_command(line):
        return commands.C

    # TODO: FIX
    raise Exception('NO RECOGNIZED')


def _is_l_command(line):
    """
    Determines if a line is a L command

    Parameters
    ----------
    line : str

    Returns
    -------
    is_l_command : bool
    """
    return line[0] == '(' and line [-1] == ')'


def _is_a_command(line):
    """
    Determines if a line is an A command

    Parameters
    ----------
    line : str

    Returns
    -------
    is_a_command : bool
    """
    return line[0] == '@'


def _is_c_command(line):
    """
    Determines if a line is a C command

    Parameters
    ----------
    line : str

    Returns
    -------
    is_c_command : bool
    """
    return True
    return line[0] == '(' and line [-1] == ')'


def _get_variable_name(line):
    """
    Parses variable name from declaration.

    Parameters
    ----------
    line : str

    Returns
    -------
    variable_name : str
    """
    return line[1:]


def _get_label_name(line):
    """
    Parses label name from declaration.

    Parameters
    ----------
    line : str

    Returns
    -------
    label_name : str
    """
    return re.sub('[()]', '', line)


def _remove_whitespacing(line):
    """
    Removes whitespacing from line.

    Parameters
    ----------
    line : str

    Returns
    -------
    line : str
    """
    return ''.join(line.split())


def _remove_comments(line):
    """
    Removes comments from line.

    Parameters
    ----------
    line : str

    Returns
    -------
    line : str
    """
    return line.split('//')[0]


def _is_valid_symbol(symbol):
    """
    Validates whether a symbol declaration is valid or not.

    Parameters
    ----------
    symbol : str

    Returns
    -------
    is_valid : bool
    """
    return re.search(r'^[a-zA-Z$:_.][a-zA-Z0-9$:_.]*$', symbol) is not None
