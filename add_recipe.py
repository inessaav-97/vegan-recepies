#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_recipe.py
Automation script to add a new recipe from an albo.inc link.

Usage:
    py -3 -I add_recipe.py <albo.inc_url>

Example:
    py -3 -I add_recipe.py https://albo.inc/post/abc123

The script will:
1. Fetch the recipe data from the albo.inc API
2. Ask you for the recipe details (title in PT, category, etc.)
3. Create the markdown file
4. Download the image
5. Update mkdocs.yml and lista.js
6. Build and deploy to GitHub Pages
"""
import sys, os, re, json, urllib.request, unicodedata, subprocess, locale

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, 'docs')
IMGS_DIR = os.path.join(DOCS_DIR, 'imagens')
CDN      = "https://cdn.albo.inc/file/sortd-images-kq4508yjh/"

CATEGORY_DIRS = {
    'pratos-principais': os.path.join(DOCS_DIR, 'pratos-principais'),
    'sopas':             os.path.join(DOCS_DIR, 'sopas'),
    'sobremesas':        os.path.join(DOCS_DIR, 'sobremesas'),
}

CATEGORY_PT = {
    'pratos-principais': 'Pratos Principais',
    'sopas':             'Sopas',
    'sobremesas':        'Sobremesas',
}

# mkdocs.yml markers — insert new entry before this line in each section
CATEGORY_MARKERS = {
    'pratos-principais': '  - Sopas:',
    'sopas':             '  - Sobremesas:',
    'sobremesas':        '  - 🔍 Pesquisa',
}


def slugify(text):
    """Convert a Portuguese title to a filesystem-safe slug."""
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')  # strip accents
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def sort_key(text):
    """Accent-insensitive, case-insensitive sort key for Portuguese titles."""
    text = unicodedata.normalize('NFD', text.lower())
    return ''.join(c for c in text if unicodedata.category(c) != 'Mn')


def fetch_albo_recipe(url):
    """Fetch recipe data from an albo.inc URL via the proxy API."""
    # Extract ID from URL patterns:
    #   https://albo.inc/post/<id>
    #   https://albo.inc/recipe/<id>
    #   https://albo.inc/<anything>/<id>
    match = re.search(r'albo\.inc/[^/]+/([a-zA-Z0-9_-]+)', url)
    if not match:
        # Try treating the last path component as an ID
        match = re.search(r'albo\.inc/([a-zA-Z0-9_-]+)$', url)
    if not match:
        print("Could not extract ID from URL. Please check the URL format.")
        sys.exit(1)

    recipe_id = match.group(1)
    api_url = f"https://albo.inc/api/proxy/imports/{recipe_id}"
    print(f"Fetching from API: {api_url}")

    req = urllib.request.Request(
        api_url,
        headers={
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json',
        }
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))

    return data


def ask(prompt, default=None):
    """Ask user for input with optional default."""
    if default:
        value = input(f"{prompt} [{default}]: ").strip()
        return value if value else default
    return input(f"{prompt}: ").strip()


def choose_category():
    """Prompt user to choose a recipe category."""
    print("\nCategoria:")
    print("  1. Pratos Principais")
    print("  2. Sopas")
    print("  3. Sobremesas")
    choice = ask("Escolha (1/2/3)", "1")
    return {
        '1': 'pratos-principais',
        '2': 'sopas',
        '3': 'sobremesas',
    }.get(choice, 'pratos-principais')


def choose_cuisine():
    """Prompt user for cuisine type."""
    cuisines = [
        'Portuguesa', 'Italiana', 'Asiática', 'Indiana', 'Mediterrânea',
        'Chinesa', 'Japonesa', 'Mexicana', 'Americana', 'Francesa',
        'Britânica', 'Russa', 'Fusão',
    ]
    print("\nCozinha:")
    for i, c in enumerate(cuisines, 1):
        print(f"  {i:2d}. {c}")
    choice = input("Número ou nome da cozinha: ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(cuisines):
            return cuisines[idx]
    except ValueError:
        pass
    return choice if choice else 'Fusão'


def choose_difficulty():
    """Prompt user for difficulty level."""
    print("\nDificuldade:")
    print("  1. Fácil")
    print("  2. Médio")
    print("  3. Difícil")
    choice = ask("Escolha (1/2/3)", "1")
    return {'1': 'Fácil', '2': 'Médio', '3': 'Difícil'}.get(choice, 'Fácil')


def build_markdown(title_pt, slug, category, cuisine, difficulty, img_filename,
                   ingredients_text, steps_text):
    """Build the full markdown content for a recipe."""
    cat_pt = CATEGORY_PT[category]
    img_ref = f"../imagens/{img_filename}"

    lines = [
        f"# {title_pt}",
        "",
        f"![{title_pt}]({img_ref})",
        "",
        "## Informação",
        "",
        f"- Categoria: {cat_pt}",
        f"- Cozinha: {cuisine}",
        f"- Dificuldade: {difficulty}",
        "",
        "## Ingredientes",
        "",
    ]

    # Ingredients: each line should be a list item
    for line in ingredients_text.strip().splitlines():
        line = line.strip()
        if line:
            if not line.startswith('-'):
                line = f"- {line}"
            lines.append(line)

    lines += ["", "## Preparação", ""]

    # Steps: numbered list
    step_lines = [l.strip() for l in steps_text.strip().splitlines() if l.strip()]
    for i, step in enumerate(step_lines, 1):
        # Strip any existing numbering
        step = re.sub(r'^[\d]+[.)]\s*', '', step)
        lines.append(f"{i}. {step}")

    lines.append("")
    return "\n".join(lines)


def download_image(img_filename):
    """Download an image from CDN."""
    dest = os.path.join(IMGS_DIR, img_filename)
    if os.path.exists(dest):
        print(f"  Imagem já existe: {img_filename}")
        return
    url = CDN + img_filename
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
        f.write(resp.read())
    print(f"  Imagem guardada: {img_filename}")


def update_galeria_js(title_pt, slug, img_filename):
    """Add new pratos-principais recipe to galeria.js in alphabetical order."""
    js_path = os.path.join(DOCS_DIR, 'javascripts', 'galeria.js')
    with open(js_path, encoding='utf-8') as f:
        text = f.read()

    if slug in text:
        print("  galeria.js: já contém esta receita.")
        return

    safe_title = title_pt.replace("'", "\\'")
    new_entry = f"  {{ nome: '{safe_title}', img: '{img_filename}', slug: '{slug}' }},\n"

    # Find all existing entries and their positions, insert alphabetically
    pattern = re.compile(r"  \{ nome: '([^']+)',.*?\},\n", re.DOTALL)
    matches = list(pattern.finditer(text))

    insert_pos = None
    for m in matches:
        existing_nome = m.group(1)
        if sort_key(title_pt) < sort_key(existing_nome):
            insert_pos = m.start()
            break

    if insert_pos is None:
        # Insert before closing ];
        insert_pos = text.rindex('];')

    text = text[:insert_pos] + new_entry + text[insert_pos:]

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("  galeria.js actualizado.")


def update_mkdocs(nav_title, slug, category):
    """Add new recipe to mkdocs.yml navigation in alphabetical order."""
    yml_path = os.path.join(BASE_DIR, 'mkdocs.yml')
    with open(yml_path, encoding='utf-8') as f:
        text = f.read()

    if slug in text:
        print("  mkdocs.yml: já contém esta receita.")
        return

    new_line = f"    - {nav_title}: {category}/{slug}.md\n"

    # Find the category section and all its recipe entries
    # Recipe entries in a section look like:    - Title: category/slug.md
    entry_pattern = re.compile(
        rf'(    - [^\n]+: {re.escape(category)}/[^\n]+\.md\n)'
    )
    matches = list(entry_pattern.finditer(text))

    insert_pos = None
    for m in matches:
        # Extract title from "    - Title: path"
        line = m.group(1)
        existing_title = re.match(r'    - (.+?): ', line).group(1)
        if sort_key(nav_title) < sort_key(existing_title):
            insert_pos = m.start()
            break

    if insert_pos is None:
        # Insert before the next category marker
        marker = CATEGORY_MARKERS[category]
        insert_pos = text.index(marker)

    text = text[:insert_pos] + new_line + text[insert_pos:]

    with open(yml_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("  mkdocs.yml actualizado.")


def update_lista_js(title_pt, slug, category):
    """Add new recipe entry to TODAS_RECEITAS in lista.js in alphabetical order."""
    js_path = os.path.join(DOCS_DIR, 'javascripts', 'lista.js')
    with open(js_path, encoding='utf-8') as f:
        text = f.read()

    if slug in text:
        print("  lista.js: já contém esta receita.")
        return

    safe_title = title_pt.replace("'", "\\'")
    new_entry = f"  {{ nome: '{safe_title}', slug: '{slug}', cat: '{category}' }},\n"

    # Find all entries of same category and insert alphabetically within the group
    cat_pattern = re.compile(
        rf"  \{{ nome: '([^']+)', slug: '[^']+', cat: '{re.escape(category)}' \}},\n"
    )
    matches = list(cat_pattern.finditer(text))

    insert_pos = None
    for m in matches:
        existing_nome = m.group(1)
        if sort_key(title_pt) < sort_key(existing_nome):
            insert_pos = m.start()
            break

    if insert_pos is None:
        if matches:
            # Insert after the last entry of this category
            last = matches[-1]
            insert_pos = last.end()
        else:
            # Category not found yet — insert before ];
            insert_pos = text.rindex('];')

    text = text[:insert_pos] + new_entry + text[insert_pos:]

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("  lista.js actualizado.")


def deploy():
    """Build MkDocs and push to GitHub to trigger deployment."""
    answer = ask("\nDeployer para o GitHub Pages agora? (s/n)", "s")
    if answer.lower() not in ('s', 'sim', 'y', 'yes'):
        print("Deploy ignorado. Execute manualmente: git add -A && git commit && git push")
        return

    print("\nA fazer deploy...")
    cmds = [
        ['git', 'add', '-A'],
        ['git', 'commit', '-m', 'feat: adicionar nova receita via add_recipe.py\n\nCo-Authored-By: Claude <noreply@anthropic.com>'],
        ['git', 'push'],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  Erro ao executar {' '.join(cmd)}:")
            print(result.stderr)
            return
        print(f"  {' '.join(cmd)} — OK")
    print("  Deploy iniciado! O GitHub Actions publicará o site em breve.")


def main():
    if len(sys.argv) < 2:
        print("Uso: py -3 -I add_recipe.py <URL>")
        print("Exemplo: py -3 -I add_recipe.py https://albo.inc/post/abc123")
        sys.exit(1)

    url = sys.argv[1]

    # ── 1. Fetch data from API ──────────────────────────────────────────────
    print(f"\nA obter dados de: {url}")
    try:
        data = fetch_albo_recipe(url)
    except Exception as e:
        print(f"Erro ao obter dados da API: {e}")
        print("Irá introduzir os dados manualmente.")
        data = {}

    # Show what we got
    orig_title = data.get('title', '')
    description = data.get('description', '')
    image_url = data.get('image', '')
    if isinstance(image_url, dict):
        image_url = image_url.get('url', '')

    print(f"\nTítulo original: {orig_title}")
    print(f"Imagem: {image_url}")
    if description:
        print(f"Descrição (primeiros 300 chars): {description[:300]}...")

    # Extract image filename from CDN URL
    img_filename = ''
    if image_url:
        img_filename = image_url.split('/')[-1]
        if '?' in img_filename:
            img_filename = img_filename.split('?')[0]

    # ── 2. Gather recipe details from user ────────────────────────────────
    print("\n--- Preencher os dados da receita ---")
    title_pt = ask("Título em Português", orig_title)
    slug_default = slugify(title_pt)
    slug = ask("Slug do ficheiro (sem .md)", slug_default)
    category = choose_category()
    cuisine = choose_cuisine()
    difficulty = choose_difficulty()

    if not img_filename:
        img_filename = ask("Nome do ficheiro da imagem (ex: abc123.jpg)")

    print("\nIngredientes (introduza cada ingrediente numa linha; linha em branco para terminar):")
    ing_lines = []
    while True:
        line = input("  - ")
        if not line.strip():
            break
        ing_lines.append(line.strip())
    ingredients_text = "\n".join(f"- {l}" for l in ing_lines)

    print("\nPassos de preparação (introduza cada passo numa linha; linha em branco para terminar):")
    step_lines = []
    while True:
        line = input(f"  {len(step_lines)+1}. ")
        if not line.strip():
            break
        step_lines.append(line.strip())
    steps_text = "\n".join(step_lines)

    # ── 3. Build and write markdown ───────────────────────────────────────
    md_content = build_markdown(
        title_pt, slug, category, cuisine, difficulty,
        img_filename, ingredients_text, steps_text
    )
    dest_dir = CATEGORY_DIRS[category]
    dest_path = os.path.join(dest_dir, slug + '.md')

    if os.path.exists(dest_path):
        overwrite = ask(f"Ficheiro {slug}.md já existe. Substituir? (s/n)", "n")
        if overwrite.lower() not in ('s', 'sim', 'y'):
            print("Operação cancelada.")
            sys.exit(0)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"\n  Ficheiro criado: {category}/{slug}.md")

    # ── 4. Download image ─────────────────────────────────────────────────
    if img_filename:
        try:
            download_image(img_filename)
        except Exception as e:
            print(f"  Aviso: não foi possível descarregar a imagem: {e}")
            print(f"  Coloque manualmente a imagem em docs/imagens/{img_filename}")

    # ── 5. Update mkdocs.yml ──────────────────────────────────────────────
    update_mkdocs(title_pt, slug, category)

    # ── 6. Update lista.js ────────────────────────────────────────────────
    update_lista_js(title_pt, slug, category)

    # ── 7. Update galeria.js (pratos principais only) ─────────────────────
    if category == 'pratos-principais':
        update_galeria_js(title_pt, slug, img_filename)

    print(f"\nReceita '{title_pt}' adicionada com sucesso!")

    # ── 8. Optional deploy ────────────────────────────────────────────────
    deploy()


if __name__ == '__main__':
    main()
