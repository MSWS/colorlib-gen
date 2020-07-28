//
// This file was generated with color_gen.py and should not be used outside of colorlib.inc
//
// Do not edit! Regenerate this file with color_gen.py
//

#if defined _{{ file_name }}_included
    #endinput
#endif
#define _{{ file_name }}_included

enum {{ enum_name }}
{
{%- for (enum, value) in colors %}
    {{ enum_name }}_{{ enum }} = {{ value }},
{%- endfor %}
};

{{ enum_name }} {{ function_name }}(char color[16])
{
{%- for (depth, key, value) in decisions recursive %}
    {%- if loop.index == 1 %}
    if (color[{{ depth }}] == {% if key is string -%} '{{ key }}' {%- else -%} {{ key }} {%- endif %})
    {
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}_{{ value }};
        {%- endif %}
    }
    {%- else %}
    else if (color[{{ depth }}] == {% if key is string -%} '{{ key }}' {%- else -%} {{ key }} {%- endif %})
    {
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}_{{ value }};
        {%- endif %}
    }
    {%- endif %}
{%- endfor %}

    return view_as<{{ enum_name }}>(0x00);
}
