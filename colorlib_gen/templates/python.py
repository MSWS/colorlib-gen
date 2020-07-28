from enum import Enum

class {{ enum_name }}(Enum):
{%- for (enum, value) in colors %}
    {{ enum }} = '{{ value }}'
{%- endfor %}

def {{ function_name }}(color : str) -> str:
{%- for (depth, key, value) in decisions recursive %}
    {%- if loop.index == 1 %}
    {%- if key is string %}
    if color[{{ depth }}] == '{{ key }}':
    {%- else %}
    if len(color) == {{ depth }}:
    {%- endif %}
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}.{{ value }}
        {%- endif %}
    {%- else %}
    {%- if key is string %}
    elif color[{{ depth }}] == '{{ key }}':
    {%- else %}
    elif len(color) == {{ depth }}:
    {%- endif %}
        {%- if value is not string -%}
        {{ loop(value)|indent(4) }}
        {%- else %}
        return {{ enum_name }}.{{ value }}
        {%- endif %}
    {%- endif %}
{%- endfor %}

    return ''