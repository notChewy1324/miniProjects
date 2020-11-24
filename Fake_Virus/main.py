# Virus Start

import sys, glob

code = []
with open(sys.argv[0], "r") as f:
    y = f.readlines

virus_area = False
for x in y:
    if x == "# Virus Start\n":
        virus_area = True
    if virus_area:
        code.append(x)
    if x == "# Virus End\n":
        break

python_scripts = glob.glob("*.py") + glob.glob("*.pyw")
print(python_scripts)

# Virus End