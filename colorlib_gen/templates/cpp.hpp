//
// This file was generated with color_gen.py and should not be used outside of colorlib.inc
//
// Do not edit! Regenerate this file with color_gen.py
//

#ifndef _{{ file_name|upper }}_HPP_
#define _{{ file_name|upper }}_HPP_

#pragma once

enum struct {{ enum_name }} : char
{
{%- for (enum, value) in colors %}
    {{ enum }} = {{ value }},
{%- endfor %}
};

inline {{ enum_name }} {{ function_name }}(char* color)
{
{%- for (depth, key, value) in decisions recursive %}
    {%- if loop.index == 1 %}
    if (color[{{ depth }}] == {% if key is string -%} '{{ key }}' {%- else -%} {{ key }} {%- endif %})
    {
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}::{{ value }};
        {%- endif %}
    }
    {%- else %}
    else if (color[{{ depth }}] == {% if key is string -%} '{{ key }}' {%- else -%} {{ key }} {%- endif %})
    {
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}::{{ value }};
        {%- endif %}
    }
    {%- endif %}
{%- endfor %}

    return static_cast<{{ enum_name }}>(0x00);
}

#endif // _{{ file_name|upper }}_HPP_
