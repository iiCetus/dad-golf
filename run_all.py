# run_all.py

import os
import subprocess

# List of your 7 script files
scripts = [
    'autoclick1.py',
    'autoclick2.py',
    'autoclick3.py',
    'autoclick4.py',
    'autoclick5.py',
    'autoclick6.py',
    'autoclick7.py',
]

for script in scripts:
    subprocess.Popen(['python', script], cwd=os.path.dirname(__file__))
