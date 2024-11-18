#!/usr/bin/env python3
"""Circle Calculator in Python."""

from math import pi as PI

radius = float(input("Radius?: "))
circum = 2.0 * PI * radius
area   = PI * radius**2

print(f"Radius : {radius:10.2f}")
print(f"Circum.: {circum:10.2f}")
print(f"Area   : {area  :10.2f}")
