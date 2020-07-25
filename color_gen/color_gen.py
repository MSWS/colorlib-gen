#! /usr/bin/env python3

import argparse
import re
import sys

import yaml

from char_group import CharGroup
from defs import DEFAULT_COLOR, COLORS, TAB

colors = []
color_enum_names = {}

defs = {}

def get_indent(i : int) -> str:
    """Returns indentation to a given level."""
    if i < 1: # no indentation needed
        return ""
    
    indent = TAB
    for i in range(1, i):
        indent = indent + TAB

    return indent

def get_hex(i : int, n : int = 2) -> str:
    """Returns a hex representation of a char."""
    return '0x' + '{:0{}x}'.format(i, n).upper()

def get_indented_def(i : int, definition : str, first : bool = True) -> str:
    """Returns an indented definition string."""
    # if the first definition in a set do not indent the first line
    if first:
        indented_def = definition[0]
    else:
        indented_def = get_indent(i) + definition[0]

    # indent the remaining lines
    for line in range(1, len(definition)):
        indented_def = indented_def + get_indent(i) + definition[line]

    return indented_def

def group_till_unique(in_group : list, i : int = 0) -> dict:
    """
    Recursively splits a list into a tree,
    where each node is a char in the leafs.
    """

    groups = {}
    for (key, group) in group_by_char_at(in_group, i).items():
        if isinstance(group, list):
            groups[key] = group_till_unique(group, i + 1)
        else:
            groups[key] = group

    return groups

def group_by_char_at(colors : list, i : int = 0) -> dict:
    """
    Returns a dictionary of strings from a list,
    grouped by the char at \'i\'.
    """

    # construnct a dictionary of strings
    # examples:
    # colors = ['default', 'darkred', 'red']
    # group_by_char_at(colors, 0)
    # { 'd': ['default', 'darkred'], 'r': ['red'] }
    #
    # colors = ['grey', 'grey2']
    # group_by_char_at(colors, 4)
    # { 0: ['grey'], '2': ['grey2'] }

    groups = {}
    for color in colors:
        if len(color) == i:
            # index greater than length of string so use null terminator
            groups[0] = color
        elif color[i] in groups:
            if isinstance(groups[color[i]], list):
                groups[color[i]].append(color)
            else:
                groups[color[i]] = [groups[color[i]], color]
        else:
            groups[color[i]] = color

    return groups

def skip_redundant_decisions(group : dict, depth : int = 0):
    """Optimisation step which skips redundant decisions."""
    # FROM:
    # 't':
    # {
    #     'e':
    #     {
    #         'a':
    #         {
    #             'm':
    #             {
    #                 ' ':
    #                 {
    #                     '0': ['team 0'],
    #                     '1': ['team 1'],
    #                     '2': ['team 2']
    #                 },
    #                 'c': ['teamcolor']
    #             }
    #         }
    #     }
    # }
    # TO:
    # (0)
    # 't':
    # {   (4)
    #     ' ':
    #     {
    #         (5)
    #         '0': ['team 0'],
    #         '1': ['team 1'],
    #         '2': ['team 2']
    #     },
    #     'c': ['teamcolor']
    # }

    if isinstance(group, dict):
        if len(group) == 1:
            for (_, value) in group.items():
                char_group = skip_redundant_decisions(value, depth + 1)
        else:
            new_group = {}
            for (key, value) in group.items():
                new_group[key] = skip_redundant_decisions(value, depth + 1)

            char_group = CharGroup(depth, new_group)
    else:
        char_group = group

    return char_group

def create_enum() -> str:
    """Creates the definition for the enum for the mapping function."""
    ev = []
    for color in colors:
        name = defs['color_name'].format(color[0].replace(' ', '_').capitalize())
        value = get_hex(color[1])
        color_enum_names[color[0]] = name
        ev.append(defs['enum_entry'].format(name, value))

    enums = ""
    for enum in ev:
        enums = enums + enum

    return defs['enum'].format(enums)

def create_return(value : str) -> str:
    """Creates a return statement."""
    return defs['return'].format(value)

def create_statement(definition : str,
                     indent : int,
                     index : int,
                     key,
                     ret : str,
                     first : bool = True) -> str:
    """Creates a statement (\'if\', \'else if\')."""
    if isinstance(key, str):
        char = defs['char'].format(key)
    else:
        char = hex(key)

    return get_indented_def(
        indent,
        definition,
        first
        ).format(index, char, ret)

def create_if(indent : int, index : int, key, ret : str) -> str:
    """Creates an \'if\' statement."""
    return create_statement(defs['if'], indent, index, key, ret, True)

def create_elif(indent : int, index : int, key, ret : str) -> str:
    """Creates an \'else if\' statement."""
    return create_statement(defs['elif'], indent, index, key, ret, False)

def create_decisions(group : CharGroup, indent : int = 0) -> str:
    """Creates the decisions for the mapping function."""
    decisions = ""
    for i, (key, value) in enumerate(group.children.items()):
        if isinstance(value, CharGroup):
            body = create_decisions(value, indent + 1)
        else:
            body = create_return(defs['enum_usage'].format(color_enum_names[value]))
        
        if i == 0:
            decisions = create_if(indent, group.depth, key, body)
        else:
            decisions = decisions + create_elif(indent, group.depth, key, body)

    return decisions


def create_map() -> str:
    """Creates the mapping function."""
    groups = group_till_unique([c[0] for c in colors])
    groups = skip_redundant_decisions(groups)

    return defs['color_function'].format(
        create_decisions(groups), 
        create_return(defs['cast'].format(get_hex(0)))
        )

def parse_definition(definition, indent : bool = False, as_list : bool = False):
    """Parses a code definition so that is in the correct format for Color Gen."""
    if as_list:
        out_def = []
    else:
        out_def = ""
    
    if type(definition) is list:
        for i in range(len(definition)):
            if indent:
                line = TAB + definition[i]
            else:
                line = definition[i]

            if as_list:
                out_def.append(line)
            else:
                out_def = out_def + line
    else:
        if indent:
            out_def = TAB + definition
        else:
            out_def = definition
    
    return out_def

def parse_definitions(target : str):
    file = open('defs/' + target + '.yaml', 'r')
    cfg = yaml.load(file, Loader=yaml.Loader)

    defs['header']         = parse_definition(cfg['header'])
    defs['footer']         = parse_definition(cfg['footer'])
    defs['color_function'] = parse_definition(cfg['color_function'])
    defs['color_name']     = parse_definition(cfg['color_name'])
    defs['enum']           = parse_definition(cfg['enum'])
    defs['enum_entry']     = parse_definition(cfg['enum_entry'], True)
    defs['enum_usage']     = parse_definition(cfg['enum_usage'])
    defs['if']             = parse_definition(cfg['if'], True, True)
    defs['elif']           = parse_definition(cfg['elif'], True, True)
    defs['else']           = parse_definition(cfg['else'], True, True)
    defs['char']           = parse_definition(cfg['char'])
    defs['cast']           = parse_definition(cfg['cast'])
    defs['return']         = parse_definition(cfg['return'], True)

def parse_config(file, include_ref_colors : bool):
    """Parses ColorGen's the YAML config file."""
    cfg = yaml.load(file, Loader=yaml.Loader)

    ref_colors = {}
    if 'ref_colors' in cfg:
        for (key, value) in cfg['ref_colors'].items():
            if isinstance(value, int):
                ref_colors[key] = value
            else:
                assert value not in COLORS, 'value is not a default engine color or integer value' 
                ref_colors[key] = COLORS[value]

    for (key, value) in cfg['colors'].items():
        if isinstance(value, int):
            colors.append((key, value))
        else:
            if value in ref_colors:
                colors.append((key, ref_colors[value]))
            elif value in COLORS:
                colors.append((key, COLORS[value]))
    
    if include_ref_colors:
        for (key, value) in ref_colors.items():
            colors.append((key, value))

def add_default_colors():
    for (key, value) in COLORS.items():
            colors.append((key, value))

def main():
    parser = argparse.ArgumentParser(description='ColorLib color map creator.')
    parser.add_argument(
        '-e',
        '--include-engine-colors',
        action="store_true",
        dest='include_engine_colors'
        )
    parser.add_argument(
        '-r',
        '--include-ref-colors',
        action="store_true",
        dest='include_ref_colors'
        )
    parser.add_argument(
        '--target',
        dest='target',
        default='sourcepawn',
        choices=['sourcepawn', 'python']
        )
    parser.add_argument(
        '--config',
        dest='config',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='config path \'{path to config dir}/color_conf.yaml\''
        )
    parser.add_argument(
        'out',
        type=argparse.FileType('w', encoding='UTF-8'),
        help='output path \'{path to include dir}/colorlib_map.inc\''
        )

    args = parser.parse_args()

    parse_definitions(args.target)

    if args.config != None:
        parse_config(args.config, args.include_ref_colors)
    else:
        colors.append(DEFAULT_COLOR)
    
    if args.include_engine_colors or args.config == None:
        add_default_colors()

    args.out.write(defs['header'])
    args.out.write(create_enum())
    args.out.write('\n')
    args.out.write(create_map())
    args.out.write(defs['footer'])
    
    args.out.close()

if __name__ == '__main__':
    main()
