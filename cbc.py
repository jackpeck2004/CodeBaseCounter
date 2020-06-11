#!/usr/bin/env python3

import os
import sys
from pathlib import Path

counter = 0

toIgnore = ["node_modules", "__pycache__", ".cache"]

dd = sys.argv[1]

for path in Path(dd).rglob('*.*'):
    pathArr = str(path).split("/")
    if not any([True for e in pathArr if e in toIgnore]):
        with open("{}/{}".format(dd, path.name), 'r') as f:
            for _ in f:
                counter += 1

print(counter)
