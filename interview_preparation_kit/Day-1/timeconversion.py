
#!/bin/python3

import math
import os
import random
import re
import sys


s=input()

hours = int(s[:2])

check_am_pm = s[-2:]

remaining_data=s[2:8]

add_values = hours % 12

# print(add_values)

if check_am_pm == "PM":

    hours = add_values + 12
    print(f"{hours:02}{remaining_data}")

if check_am_pm == "AM":

    hours = add_values
    print(f"{hours:02}{remaining_data}")