<h1 align="center">
    ColorLib - Color Generator
</h1>
<p align="center">
    <strong>A tool which generates decision trees for accelerated string lookup
    in ColorLib.</strong>
</p>

ColorLib - Color Generator creates accelerated string lookup functions for
ColorLib from a set of input colors, it creates a minimum spanning decision tree
to identify any color in the input set.

The decision tree is then converted into the neccesary source code for the use
case and included in one of the ColorLibs implementations.

## Usage
First you need to install `colorlib_gen` with `py ./setup.py install`.

To change the output colors you first need to create a new or edit your config
file.

There is an example config file provided that it is recommended you copy from it
can be seen [here](example_conf.yaml).

Then you can rerun `colorlib_gen` to generate a new file containing a lookup
function for your colors.

#### Example
```bash
# for more info use ./color_gen.py -h
colorlib_gen -re --target "sourcepawn" --config "./example_conf.yaml" "./colorlib_map.inc"
```

#### Example GitHub workflow for SourcePawn
__Note:__ _This must executed before the plugins will be compiled._
```yaml
- name: Generate colorlib_map.inc
  run:
    - python3 ./setup.py install
    - colorlib_gen -r --config "./example_conf.yaml" "../include/colorlib_map.inc"
  working-directory: ./tools
```

## Download
 - https://github.com/c0rp3n/colorlib-gen
