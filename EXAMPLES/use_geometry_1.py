import sys
import os
import geometry
# find geometry.py and execute its code

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search order
#  1. current folder
#  2. folders in PYTHONPATH
#  3. folders in sys.prefix/lib/...  (installation folder)
print(f"{sys.prefix = }")
print(sorted(os.listdir(sys.prefix + '/lib')))
print()
