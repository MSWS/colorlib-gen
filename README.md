<h1 align="center">
    ColorLib - Color Generator
</h1>
<p align="center">
    <strong>A tool which generates decision trees for accelerated string lookup in ColorLib.</strong>
</p>

ColorLib - Color Generator creates accelerated string lookup functions for ColorLib from a set of input colors, it creates a minimum spanning decision tree to identify any color in the input set.

The decision tree is then converted into the neccesary code for the use case and included in one of the ColorLib implementations.

## Status

*This project is still under active development and has not yet reached a stable
version until v1.0.0 So when using this code currently expect random error and
dragons.*

## Usage
To change the output colors you first need to create a new or edit your config
file.

There is an example config file provided that it is recommended you copy from it
can be seen [here](tools/example_conf.yaml).

Then you can rerun `color_gen.py` to generate a new `colorlib_map.inc` to
replace the default one provided.

#### Example
```bash
# for more info use ./color_gen.py -h
./color_gen.py -r --config "./example_conf.yaml" "./colorlib_map.inc"
```

#### Example GitHub workflow
__Note:__ _This must executed before the plugins will be compiled._
```yaml
- name: Generate colorlib.inc
  run: python3 ./color_gen.py -r --config "./example_conf.yaml" "../addons/sourcemod/scripting/include/colorlib_map.inc"
  working-directory: ./tools
```

## Download
 - https://github.com/c0rp3n/color-gen
