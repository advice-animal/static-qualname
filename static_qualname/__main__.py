from pathlib import Path
import sys

from . import Env

e = Env()
for dir in sys.path:
    p = Path(dir)
    if p.exists():
        e.add_site_packages(p)

print(e.real_qualname(sys.argv[1]))
