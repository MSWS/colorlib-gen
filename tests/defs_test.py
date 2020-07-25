#! /usr/bin/env python3

import yaml

TAB = "    "

HEADER = (
    "//\n" +
    "// This file was generated with color_gen.py and should not be used outside of colorlib.inc\n" +
    "//\n" +
    "// Do not edit! Regenerate this file with color_gen.py\n" +
    "//\n" +
    "\n" +
    "#if defined _colorlib_map_included\n" +
    TAB + "#endinput\n" +
    "#endif\n" +
    "#define _colorlib_map_included\n" +
    "\n"
    )

FOOTER = (
    "\n"
    )

ENUM_DEF = (
    "enum CL_Colors\n" +
    "{{\n" +
    "{}" +
    "}};\n"
    )

ENUM_ENTRY_DEF = TAB + "{} = {},\n"

COLOR_FUNCTION_DEF = (
    "CL_Colors _CL_ColorMap(char color[16])\n" +
    "{{\n" +
    "{}" +
    "\n" +
    "{}" +
    "}}\n"
    )

IF_DEF = [
    TAB + "if (color[{}] == {})\n",
    TAB + "{{\n",
    TAB + "{}",
    TAB + "}}\n"
    ]

ELIF_DEF = [
    TAB + "else if (color[{}] == {})\n",
    TAB + "{{\n",
    TAB + "{}",
    TAB + "}}\n"
    ]

ELSE_DEF = [
    TAB + "else\n",
    TAB + "{{\n",
    TAB + "{}",
    TAB + "}}\n"
    ]

CHAR_DEF = "\'{}\'"

VIEW_AS_DEF = "view_as<CL_Colors>({})"

RETURN_DEF = TAB + "return {};\n"

def test(name : str, a : str, b : str) -> None:
    if a == b:
        print("[SUCCESS] " + name)
    else:
        print("[FAILURE] " + name)

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

def main():
    """Tests whether the base SourcePawn config input defs are correct."""
    file = open('defs/sourcepawn.yaml', 'r')
    cfg = yaml.load(file, Loader=yaml.Loader)

    test("Header", HEADER, parse_definition(cfg['header'], False))
    test("Footer", FOOTER, parse_definition(cfg['footer'], False))
    test("Color function", COLOR_FUNCTION_DEF, parse_definition(cfg['color_function'], False))
    test("Enum", ENUM_DEF, parse_definition(cfg['enum'], False))
    test("Enum entry", ENUM_ENTRY_DEF, parse_definition(cfg['enum_entry'], True))
    test("If statement", IF_DEF, parse_definition(cfg['if'], True, True))
    test("Elif statement", ELIF_DEF, parse_definition(cfg['elif'], True, True))
    test("Else statement", ELSE_DEF, parse_definition(cfg['else'], True, True))
    test("Char", CHAR_DEF, parse_definition(cfg['char'], False))
    test("Cast", VIEW_AS_DEF, parse_definition(cfg['cast'], False))
    test("Return statement", RETURN_DEF, parse_definition(cfg['return'], True))
    
if __name__ == '__main__':
    main()
