const TODAS_RECEITAS = [
  { nome: 'Arroz Salteado Oriental com Tofu e Cajus', slug: 'arroz-salteado-tofu-cajus', cat: 'pratos-principais' },
  { nome: 'Barcos de Curgete Pizza', slug: 'barcos-de-curgete-pizza', cat: 'pratos-principais' },
  { nome: 'Bifes de Couve-flor Panados', slug: 'bifes-de-couve-flor-panados', cat: 'pratos-principais' },
  { nome: 'Bowl de Edamame com Arroz de Sushi', slug: 'bowl-edamame-sushi', cat: 'pratos-principais' },
  { nome: 'Caril Massaman', slug: 'caril-massaman', cat: 'pratos-principais' },
  { nome: 'Chow Mein', slug: 'chow-mein', cat: 'pratos-principais' },
  { nome: 'Esparguete com Pesto de Tofu', slug: 'esparguete-pesto-tofu', cat: 'pratos-principais' },
  { nome: 'Feijocas com Leite de Coco e Espinafres', slug: 'feijocas-leite-coco-espinafres', cat: 'pratos-principais' },
  { nome: 'Gnocchi com Creme de Castanha e Tomates', slug: 'gnocchi-creme-castanha-tomates', cat: 'pratos-principais' },
  { nome: 'Gnocchi com Tomates, Lentilhas e Tofu', slug: 'gnocchi-tomates-lentilhas', cat: 'pratos-principais' },
  { nome: 'Lentilhas Cremosas com Espinafre', slug: 'lentilhas-cremosas-espinafre', cat: 'pratos-principais' },
  { nome: 'Massa com Pimento Vermelho Assado', slug: 'massa-com-pimento-vermelho-assado', cat: 'pratos-principais' },
  { nome: 'Massa Cremosa com Cogumelos e Miso', slug: 'massa-cogumelos-miso', cat: 'pratos-principais' },
  { nome: 'Nachos com Feijão Preto e Guacamole', slug: 'nachos-feijao-preto', cat: 'pratos-principais' },
  { nome: 'Orzo com Tomates Secos e Tofu', slug: 'orzo-tomates-secos-tofu', cat: 'pratos-principais' },
  { nome: 'Queques de Tofu com Tomate Seco', slug: 'queques-tofu-tomate-seco', cat: 'pratos-principais' },
  { nome: 'Quiche de Batata com Tofu e Legumes', slug: 'quiche-batata-tofu', cat: 'pratos-principais' },
  { nome: 'Ramen de Legumes', slug: 'ramen-de-legumes', cat: 'pratos-principais' },
  { nome: 'Salada de Falafel no Forno', slug: 'salada-de-falafel-no-forno', cat: 'pratos-principais' },
  { nome: 'Shawarma de Cogumelos', slug: 'shawarma-de-cogumelos', cat: 'pratos-principais' },
  { nome: 'Tofu com Sésamo e Brócolos', slug: 'tofu-sesamo-broculos', cat: 'pratos-principais' },
  { nome: 'Tofu Salteado com Legumes', slug: 'tofu-salteado-legumes', cat: 'pratos-principais' },
  { nome: 'Udon Cremoso com Tofu', slug: 'udon-cremoso-tofu', cat: 'pratos-principais' },
];

const STORAGE_KEY = 'lista_compras_items';
const selecao = new Set();

// ── Ingredient parser ───────────────────────────

const FRACTIONS = { '½': 0.5, '¼': 0.25, '¾': 0.75, '⅓': 1/3, '⅔': 2/3 };

const UNIT_PATTERNS = [
  [/^colheres?\s+de\s+sopa\s+(?:de\s+)?/i,  'c.s.'],
  [/^colheres?\s+de\s+chá\s+(?:de\s+)?/i,   'c.c.'],
  [/^c\.?\s*s\.?\s+(?:de\s+)?/i,            'c.s.'],
  [/^c\.?\s*c\.?\s+(?:de\s+)?/i,            'c.c.'],
  [/^chávenas?\s+de\s+chá\s+(?:de\s+)?/i,   'chávena de chá'],
  [/^chávenas?\s+(?:de\s+)?/i,              'chávena'],
  [/^kg\s+(?:de\s+)?/i,                     'kg'],
  [/^g\s+(?:de\s+)?/i,                      'g'],
  [/^ml\s+(?:de\s+)?/i,                     'ml'],
  [/^dl\s+(?:de\s+)?/i,                     'dl'],
  [/^l(?:itros?)?\s+(?:de\s+)?/i,           'l'],
  [/^latas?\s+(?:de\s+)?/i,                 'lata'],
  [/^dentes?\s+(?:de\s+)?/i,               'dente'],
  [/^ramos?\s+(?:de\s+)?/i,                 'ramo'],
  [/^folhas?\s+(?:de\s+)?/i,               'folha'],
  [/^embalagens?\s+(?:de\s+)?/i,           'embalagem'],
  [/^pacotes?\s+(?:de\s+)?/i,              'pacote'],
];

function stripPrep(text) {
  return text
    .split(',')[0]                                                                            // drop everything after first comma
    .replace(/\s+(a\s+gosto|q\.?\s*b\.?)\s*$/i, '')                                          // "a gosto", "q.b."
    .replace(/\s+em\s+\w+(\s+\w+)?\s*$/i, '')                                                // "em rodelas", "em cubos"
    .replace(/\s+(picad[ao]s?|cortad[ao]s?|fatiados?|laminad[ao]s?|ralad[ao]s?|partido[s]?|amassad[ao]s?|esmagad[ao]s?|descascad[ao]s?|cozid[ao]s?|escorridos?|temperados?)\s*$/i, '')
    .trim();
}

function parseIngredient(raw) {
  let text = stripPrep(raw);

  // Parse leading fraction or number
  let qty = null;
  const fracMatch = text.match(/^([½¼¾⅓⅔])\s*/);
  if (fracMatch) {
    qty = FRACTIONS[fracMatch[1]] ?? null;
    text = text.slice(fracMatch[0].length);
  } else {
    const numMatch = text.match(/^(\d+(?:[.,]\d+)?)\s*/);
    if (numMatch) {
      qty = parseFloat(numMatch[1].replace(',', '.'));
      text = text.slice(numMatch[0].length);
    }
  }

  // Parse unit
  let unit = null;
  for (const [pattern, unitName] of UNIT_PATTERNS) {
    const m = text.match(pattern);
    if (m) { unit = unitName; text = text.slice(m[0].length); break; }
  }

  const name = text.toLowerCase().trim();
  return { qty, unit, name };
}

function fmtQty(qty) {
  if (qty === null) return '';
  if (Math.abs(qty - 0.5) < 0.01) return '½';
  if (Math.abs(qty - 0.25) < 0.01) return '¼';
  if (Math.abs(qty - 0.75) < 0.01) return '¾';
  if (Number.isInteger(qty)) return String(qty);
  return qty.toFixed(1);
}

function combineIngredients(allRaw) {
  const groups = new Map(); // name → [{ qty, unit }]

  allRaw.forEach(raw => {
    const { qty, unit, name } = parseIngredient(raw);
    if (!name) return;
    if (!groups.has(name)) groups.set(name, []);
    const slots = groups.get(name);
    const existing = slots.find(s => s.unit === unit);
    if (existing && qty !== null && existing.qty !== null) {
      existing.qty += qty;
    } else {
      slots.push({ qty, unit });
    }
  });

  const lines = [];
  groups.forEach((slots, name) => {
    slots.forEach(({ qty, unit }) => {
      const qPart = qty !== null ? fmtQty(qty) + ' ' : '';
      const uPart = unit ? unit + ' de ' : '';
      const label = qPart + uPart + name;
      lines.push(label.charAt(0).toUpperCase() + label.slice(1));
    });
  });
  return lines.sort((a, b) => a.localeCompare(b, 'pt'));
}

// ── Recipe selector ─────────────────────────────

function renderSelector() {
  const container = document.getElementById('recipe-selector');
  if (!container) return;
  const grid = document.createElement('div');
  grid.className = 'receita-selector-grid';
  TODAS_RECEITAS.forEach(r => {
    const label = document.createElement('label');
    label.className = 'receita-selector-item';
    label.innerHTML = `<input type="checkbox" value="${r.slug}"><span>${r.nome}</span>`;
    label.querySelector('input').addEventListener('change', e => {
      const key = r.slug + '|' + r.cat;
      if (e.target.checked) selecao.add(key);
      else selecao.delete(key);
      label.classList.toggle('selected', e.target.checked);
    });
    grid.appendChild(label);
  });
  container.appendChild(grid);
}

function selecionarTudo() {
  document.querySelectorAll('.receita-selector-item').forEach(label => {
    const cb = label.querySelector('input');
    if (!cb.checked) { cb.checked = true; cb.dispatchEvent(new Event('change')); }
  });
}

function limparSelecao() {
  selecao.clear();
  document.querySelectorAll('.receita-selector-item').forEach(label => {
    label.querySelector('input').checked = false;
    label.classList.remove('selected');
  });
  document.getElementById('shopping-list').innerHTML = '';
}

// ── Fetch ingredients from built HTML page ───────

async function fetchIngredients(slug, cat) {
  try {
    const res = await fetch(`../${cat}/${slug}/`);
    if (!res.ok) return [];
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    for (const h of doc.querySelectorAll('h2')) {
      if (h.textContent.trim().toLowerCase() === 'ingredientes') {
        const ul = h.nextElementSibling;
        if (ul && (ul.tagName === 'UL' || ul.tagName === 'OL')) {
          return Array.from(ul.querySelectorAll('li')).map(li => li.textContent.trim()).filter(Boolean);
        }
      }
    }
  } catch (e) {}
  return [];
}

// ── Generate list ────────────────────────────────

async function gerarLista() {
  if (selecao.size === 0) { alert('Seleciona pelo menos uma receita.'); return; }
  const listDiv = document.getElementById('shopping-list');
  listDiv.innerHTML = '<p class="lista-loading">A carregar ingredientes…</p>';

  const results = await Promise.all(
    Array.from(selecao).map(key => {
      const [slug, cat] = key.split('|');
      return fetchIngredients(slug, cat);
    })
  );

  const combined = combineIngredients(results.flat());
  const checked = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');

  listDiv.innerHTML = '';

  if (!combined.length) {
    listDiv.innerHTML = '<p>Não foi possível carregar os ingredientes das receitas selecionadas.</p>';
    return;
  }

  const header = document.createElement('div');
  header.className = 'lista-result-header';
  header.innerHTML = `
    <h2>Lista de Compras</h2>
    <div class="lista-result-actions">
      <button class="md-button" onclick="limparMarcacoes()">Limpar marcações</button>
      <button class="md-button" onclick="copiarLista()">Copiar lista</button>
    </div>
  `;
  listDiv.appendChild(header);

  const ul = document.createElement('ul');
  ul.className = 'lista-ingredientes';
  combined.forEach(ing => {
    const isChecked = !!checked[ing];
    const li = document.createElement('li');
    li.className = 'lista-item' + (isChecked ? ' checked' : '');
    li.innerHTML = `<label><input type="checkbox"${isChecked ? ' checked' : ''}><span>${ing}</span></label>`;
    li.querySelector('input').addEventListener('change', e => {
      const c = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      if (e.target.checked) { c[ing] = true; li.classList.add('checked'); }
      else { delete c[ing]; li.classList.remove('checked'); }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(c));
    });
    ul.appendChild(li);
  });
  listDiv.appendChild(ul);
}

function limparMarcacoes() {
  localStorage.removeItem(STORAGE_KEY);
  document.querySelectorAll('.lista-item').forEach(li => {
    li.classList.remove('checked');
    li.querySelector('input').checked = false;
  });
}

function copiarLista() {
  const lines = [];
  document.querySelectorAll('.lista-item span').forEach(span => lines.push('• ' + span.textContent));
  navigator.clipboard.writeText(lines.join('\n')).then(() => {
    const btn = document.querySelector('[onclick="copiarLista()"]');
    btn.textContent = 'Copiado!';
    setTimeout(() => btn.textContent = 'Copiar lista', 2000);
  });
}

document.addEventListener('DOMContentLoaded', renderSelector);
