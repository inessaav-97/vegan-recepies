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

// ── Unit conversion tables ──────────────────────

const TO_GRAMS  = { 'g': 1, 'kg': 1000 };
const TO_ML     = { 'ml': 1, 'l': 1000, 'dl': 100, 'c.s.': 15, 'c.c.': 5, 'chávena': 240, 'chávena de chá': 240 };

// Grams per 1 item (count) for common vegan ingredients
const ITEM_G = {
  'cogumelos': 15, 'cogumelo': 15,
  'cebola': 150, 'cebolas': 150,
  'tomate': 120, 'tomates': 120,
  'tomate cereja': 8, 'tomates cereja': 8,
  'cenoura': 60, 'cenouras': 60,
  'batata': 150, 'batatas': 150,
  'pimento': 160, 'pimentos': 160,
  'curgete': 200, 'curgetes': 200,
  'limão': 100, 'limões': 100,
  'laranja': 130, 'laranjas': 130,
};

// Grams per 1 chávena for solid ingredients (bridges count ↔ volume)
const CHAV_G = {
  'cogumelos': 75, 'cogumelo': 75,
  'espinafres': 30, 'espinafre': 30,
  'arroz': 185,
  'farinha': 120,
  'açúcar': 200,
  'grão-de-bico': 200,
  'lentilhas': 200,
  'feijão': 185, 'feijão preto': 185,
  'cajus': 130,
  'amêndoas': 145,
  'nozes': 120,
  'flocos de aveia': 90,
};

// ── Ingredient parser ───────────────────────────

const FRACS = { '½': 0.5, '¼': 0.25, '¾': 0.75, '⅓': 1/3, '⅔': 2/3 };

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
    .split(',')[0]
    .replace(/\s+(a\s+gosto|q\.?\s*b\.?)\s*$/i, '')
    .replace(/\s+em\s+\w+(\s+\w+)?\s*$/i, '')
    .replace(/\s+(picad[ao]s?|cortad[ao]s?|fatiados?|laminad[ao]s?|ralad[ao]s?|partido[s]?|amassad[ao]s?|esmagad[ao]s?|descascad[ao]s?|cozid[ao]s?|escorridos?|temperados?)\s*$/i, '')
    .trim();
}

function parseIngredient(raw) {
  let text = stripPrep(raw);
  let qty = null;
  const fracMatch = text.match(/^([½¼¾⅓⅔])\s*/);
  if (fracMatch) {
    qty = FRACS[fracMatch[1]] ?? null;
    text = text.slice(fracMatch[0].length);
  } else {
    const numMatch = text.match(/^(\d+(?:[.,]\d+)?)\s*/);
    if (numMatch) { qty = parseFloat(numMatch[1].replace(',', '.')); text = text.slice(numMatch[0].length); }
  }
  let unit = null;
  for (const [pat, u] of UNIT_PATTERNS) {
    const m = text.match(pat);
    if (m) { unit = u; text = text.slice(m[0].length); break; }
  }
  return { qty, unit, name: text.toLowerCase().trim() };
}

function fmtQty(qty) {
  if (qty === null) return '';
  if (Math.abs(qty - Math.round(qty)) < 0.08) return String(Math.round(qty));
  if (Math.abs(qty - 0.5)  < 0.08) return '½';
  if (Math.abs(qty - 0.25) < 0.08) return '¼';
  if (Math.abs(qty - 0.75) < 0.08) return '¾';
  if (Math.abs(qty - 1.5)  < 0.08) return '1½';
  if (Math.abs(qty - 2.5)  < 0.08) return '2½';
  return qty.toFixed(1);
}

// ── Unit unification ────────────────────────────

function unifySlots(slots, name) {
  const isW = u => u in TO_GRAMS;
  const isV = u => u in TO_ML;
  const isC = u => u === null;

  const families = [...new Set(slots.map(s => isW(s.unit) ? 'w' : isV(s.unit) ? 'v' : 'c'))];

  // All weight → sum in g/kg
  if (families.length === 1 && families[0] === 'w') {
    const totalG = slots.reduce((s, { qty, unit }) => s + (qty ?? 0) * TO_GRAMS[unit], 0);
    return totalG >= 1000
      ? { qty: +(totalG/1000).toFixed(2), unit: 'kg', approx: false }
      : { qty: Math.round(totalG), unit: 'g', approx: false };
  }

  // All volume → sum in ml, display in dominant unit
  if (families.length === 1 && families[0] === 'v') {
    const totalMl = slots.reduce((s, { qty, unit }) => s + (qty ?? 0) * TO_ML[unit], 0);
    const dominant = slots.reduce((best, s) =>
      (s.qty ?? 0) * TO_ML[s.unit] > (best.qty ?? 0) * TO_ML[best.unit] ? s : best
    ).unit;
    return { qty: +(totalMl / TO_ML[dominant]).toFixed(2), unit: dominant, approx: false };
  }

  // Count + chávena → convert via g
  if (families.includes('c') && families.includes('v')) {
    const itemG = ITEM_G[name];
    const chavG = CHAV_G[name];
    if (!itemG || !chavG) return null;
    let totalG = 0;
    for (const { qty, unit } of slots) {
      if (qty === null) continue;
      if (isC(unit))    totalG += qty * itemG;
      else if (unit === 'chávena' || unit === 'chávena de chá') totalG += qty * chavG;
      else return null;
    }
    return { qty: +(totalG / chavG).toFixed(1), unit: 'chávena', approx: true };
  }

  // Count + weight → convert via g
  if (families.includes('c') && families.includes('w')) {
    const itemG = ITEM_G[name];
    if (!itemG) return null;
    let totalG = 0;
    for (const { qty, unit } of slots) {
      if (qty === null) continue;
      if (isC(unit)) totalG += qty * itemG;
      else totalG += qty * TO_GRAMS[unit];
    }
    return totalG >= 1000
      ? { qty: +(totalG/1000).toFixed(2), unit: 'kg', approx: true }
      : { qty: Math.round(totalG), unit: 'g', approx: true };
  }

  return null;
}

// ── Combine ingredients ─────────────────────────

function combineIngredients(allRaw) {
  const groups = new Map();
  allRaw.forEach(raw => {
    const { qty, unit, name } = parseIngredient(raw);
    if (!name) return;
    if (!groups.has(name)) groups.set(name, []);
    const slots = groups.get(name);
    const existing = slots.find(s => s.unit === unit);
    if (existing && qty !== null && existing.qty !== null) existing.qty += qty;
    else slots.push({ qty, unit });
  });

  // Merge: single-word key absorbs longer names starting with it
  const merged = new Map();
  Array.from(groups.keys())
    .sort((a, b) => a.length - b.length)
    .forEach(name => {
      let foundKey = null;
      for (const key of merged.keys()) {
        if (name === key || (!key.includes(' ') && name.startsWith(key + ' '))) {
          foundKey = key; break;
        }
      }
      if (foundKey) {
        const existing = merged.get(foundKey);
        groups.get(name).forEach(({ qty, unit }) => {
          const slot = existing.find(s => s.unit === unit);
          if (slot && qty !== null && slot.qty !== null) slot.qty += qty;
          else existing.push({ qty, unit });
        });
      } else {
        merged.set(name, [...groups.get(name)]);
      }
    });

  const lines = [];
  merged.forEach((slots, name) => {
    let label;
    if (slots.length === 1) {
      const { qty, unit } = slots[0];
      label = qty === null
        ? name + ' (q.b.)'
        : fmtQty(qty) + (unit ? ' ' + unit + ' de ' : ' ') + name;
    } else {
      const unified = unifySlots(slots, name);
      if (unified) {
        const { qty, unit, approx } = unified;
        label = (approx ? 'aprox. ' : '') + fmtQty(qty) + (unit ? ' ' + unit + ' de ' : ' ') + name;
      } else {
        const parts = slots.map(({ qty, unit }) =>
          qty !== null ? fmtQty(qty) + (unit ? ' ' + unit : '') : 'q.b.'
        );
        label = name + ': ' + parts.join(' + ');
      }
    }
    lines.push(label.charAt(0).toUpperCase() + label.slice(1));
  });

  return lines.sort((a, b) => a.localeCompare(b, 'pt'));
}

// ── UI ──────────────────────────────────────────

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
      if (e.target.checked) selecao.add(key); else selecao.delete(key);
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

async function fetchIngredients(slug, cat) {
  try {
    const res = await fetch(`../${cat}/${slug}/`);
    if (!res.ok) return [];
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    let ingredientesHeading = null;
    for (const h of doc.querySelectorAll('h2, h3')) {
      if (h.textContent.toLowerCase().includes('ingrediente')) { ingredientesHeading = h; break; }
    }
    if (!ingredientesHeading) return [];
    const items = [];
    let sibling = ingredientesHeading.nextElementSibling;
    while (sibling) {
      if (sibling.tagName === 'H2') break;
      if (sibling.tagName === 'UL' || sibling.tagName === 'OL') {
        sibling.querySelectorAll('li').forEach(li => { const t = li.textContent.trim(); if (t) items.push(t); });
      }
      sibling = sibling.nextElementSibling;
    }
    return items;
  } catch (e) { return []; }
}

async function gerarLista() {
  if (selecao.size === 0) { alert('Seleciona pelo menos uma receita.'); return; }
  const listDiv = document.getElementById('shopping-list');
  listDiv.innerHTML = '<p class="lista-loading">A carregar ingredientes…</p>';

  const results = await Promise.all(
    Array.from(selecao).map(key => { const [slug, cat] = key.split('|'); return fetchIngredients(slug, cat); })
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
    </div>`;
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
  document.querySelectorAll('.lista-item span').forEach(s => lines.push('• ' + s.textContent));
  navigator.clipboard.writeText(lines.join('\n')).then(() => {
    const btn = document.querySelector('[onclick="copiarLista()"]');
    btn.textContent = 'Copiado!'; setTimeout(() => btn.textContent = 'Copiar lista', 2000);
  });
}

document.addEventListener('DOMContentLoaded', renderSelector);
