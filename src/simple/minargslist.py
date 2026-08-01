#!/usr/bin/env python3
import sys
print(f"Script: {sys.argv[0]}")
for n, arg in enumerate(sys.argv[1:]):
   print(f"Arg #{n + 1}: {arg}")
