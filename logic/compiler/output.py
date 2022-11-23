import basiclex
import basparse
import basinterp

with open("./logic/code.bas") as f:
    data = f.read()

prog = basparse.parse(data)
if not prog:
    raise SystemExit
b = basinterp.BasicInterpreter(prog)
try:
    b.run()
    raise SystemExit
except RuntimeError:
    pass