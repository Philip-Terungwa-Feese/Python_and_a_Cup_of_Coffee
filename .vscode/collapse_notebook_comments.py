import json
from pathlib import Path

notebook_path = Path("c:/Users/PC/Documents/Mastering_Python_From-_Beginner-_to_Pro/Python_and_a_Cup_of_Coffee/2026_Python_Programming_Notebook.ipynb")
nb = json.loads(notebook_path.read_text(encoding='utf-8'))
changed = 0

for cell in nb.get('cells', []):
    if cell.get('cell_type') != 'markdown':
        continue

    source = cell.get('source', [])
    if isinstance(source, list):
        text = ''.join(source)
    else:
        text = source

    stripped = text.strip()
    if not stripped or stripped.startswith('<details'):
        continue

    wrapped = f"<details>\n<summary>Comment</summary>\n\n{text}\n</details>"
    cell['source'] = wrapped.splitlines(keepends=True)
    cell.setdefault('metadata', {})['collapsed'] = True
    changed += 1

notebook_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(f'Updated {changed} markdown cells to collapsed details blocks.')
