# save this as decompile_with_decompyle3.py
from decompyle3.main import decompile_file
import os

input_file = os.path.join('windows.exe_extracted', 'Main.pyc')
output_file = os.path.join(os.getcwd(), 'decompiled_Main.py')

with open(output_file, 'w') as f:
    decompile_file(input_file, f)
