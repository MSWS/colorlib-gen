#!/bin/sh
git clone --single-branch --branch v2.x https://github.com/catchorg/Catch2.git
mkdir Catch2/build
cd Catch2/build
cmake -DBUILD_TESTING=OFF ..
make && sudo make install
