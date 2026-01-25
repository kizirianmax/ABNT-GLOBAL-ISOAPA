import os
import re
import markdown
from pathlib import Path

def generate_index(directory):
    index_content = "# Index\n\n"
    for filepath in Path(directory).rglob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            title_search = re.search(r'# (.*)', content)
            title = title_search.group(1) if title_search else filepath.name
            index_content += f'- [{title}](./{filepath.relative_to(directory)})\n'
    return index_content

if __name__ == '__main__':
    docs_dir = './docs'
    index_md = generate_index(docs_dir)
    with open(os.path.join(docs_dir, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(index_md)
