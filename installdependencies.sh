#!/bin/sh
# games i wrote are in a different git, run me to install them nicely :)
rm -r py
mkdir py && cd py
curl https://raw.githubusercontent.com/justinburrill/pysnake/master/snake.py --output snake.py -s
curl https://raw.githubusercontent.com/justinburrill/pypong/main/pong.py --output pong.py -s