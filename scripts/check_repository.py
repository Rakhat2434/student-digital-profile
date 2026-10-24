"""Check the tracked scaffold and local Markdown links; no third-party packages."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import os
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.next', 'dist', 'coverage'}
errors = []
layout = json.loads((ROOT / 'config/repository-layout.json').read_text(encoding='utf-8'))
for relative in layout['reservedDirectories']:
    target = (ROOT / relative).resolve()
    if not target.is_relative_to(ROOT):
        errors.append(f'Layout path escapes repository: {relative}')
    elif not target.is_dir():
        errors.append(f'Missing reserved directory: {relative}')
    elif not any(target.iterdir()):
        errors.append(f'Empty directory will be lost by Git: {relative}')

links = 0
documents = 0
for directory, subdirs, files in os.walk(ROOT):
    subdirs[:] = [d for d in subdirs if d not in SKIP]
    for name in files:
        if not name.endswith('.md'):
            continue
        document = Path(directory) / name
        text = document.read_text(encoding='utf-8-sig')
        documents += 1
        if re.search(r'^(?:<<<<<<< |=======\s*$|>>>>>>> )', text, re.M):
            errors.append(f'Unresolved conflict marker: {document.relative_to(ROOT)}')
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            href = match.group(1).strip().split(' "', 1)[0].strip('<>')
            if not href or href.startswith('#'):
                continue
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path:
                continue
            links += 1
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'Broken link in {document.relative_to(ROOT)}: {href}')

for error in errors:
    print('ERROR:', error)
print(f'Checked {len(layout["reservedDirectories"])} reserved directories, '
      f'{documents} Markdown files and {links} relative links; {len(errors)} errors.')
sys.exit(bool(errors))
