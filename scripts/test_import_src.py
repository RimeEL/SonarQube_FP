from pathlib import Path
import sys

# replicate discovery used in notebook

def find_project_root(max_up=6):
    p = Path('.').resolve()
    for _ in range(max_up):
        if (p / 'src').exists() or (p / 'README.md').exists() or (p / 'data').exists():
            return p
        p = p.parent
    return Path('.').resolve()

PROJECT_ROOT = find_project_root()
print('PROJECT_ROOT =', PROJECT_ROOT)
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
print('sys.path[0]=', sys.path[0])
try:
    from src.preprocessing import tokenize
    print('Imported src.preprocessing.tokenize OK')
except Exception as e:
    print('Import failed:', e)
    raise
