DEFAULT_COLOR = ('default', 0x01)

COLORS = {
    'engine 1':    0x01,
    'engine 2':    0x02,
    'engine 3':    0x03,
    'engine 4':    0x04,
    'engine 5':    0x05,
    'engine 6':    0x06,
    'engine 7':    0x07,
    'engine 8':    0x08,
    'engine 9':    0x09,
    'engine 10':   0x0A,
    'engine 11':   0x0B,
    'engine 12':   0x0C,
    'engine 13':   0x0D,
    'engine 14':   0x0E,
    'engine 15':   0x0F,
    'engine 16':   0x10
    }

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