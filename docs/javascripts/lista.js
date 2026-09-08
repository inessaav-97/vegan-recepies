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

function renderSelector() {
  const container = document.getElementById('recipe-selector');
  if (!container) return;
  const grid = document.createElement('div');
  grid.className = 'receita-selector-grid';
  TODAS_RECEITAS.forEach(r => {
    const label = document.createElement('label');
    label.className = 'receita-selector-item';
    label.dataset.slug = r.slug;
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
    cb.checked = true;
    cb.dispatchEvent(new Event('change'));
  });
}

function limparSelecao() {
  selecao.clear();
  document.querySelectorAll('.receita-selector-item').forEach(label => {
    label.querySelector('input').checked = false;
    label.classList.remove('selected');
  });
}

async function fetchIngredients(slug, cat) {
  try {
    const res = await fetch(`../${cat}/${slug}/`);
    if (!res.ok) return [];
    const html = await res.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
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

async function gerarLista() {
  if (selecao.size === 0) {
    alert('Seleciona pelo menos uma receita.');
    return;
  }
  const listDiv = document.getElementById('shopping-list');
  listDiv.innerHTML = '<p class="lista-loading">A carregar ingredientes…</p>';

  const results = await Promise.all(
    Array.from(selecao).map(async key => {
      const [slug, cat] = key.split('|');
      const nome = TODAS_RECEITAS.find(r => r.slug === slug)?.nome || slug;
      const ingredientes = await fetchIngredients(slug, cat);
      return { nome, slug, ingredientes };
    })
  );

  const checked = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  listDiv.innerHTML = '';

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

  let hasContent = false;
  results.forEach(({ nome, slug, ingredientes }) => {
    if (!ingredientes.length) return;
    hasContent = true;
    const section = document.createElement('div');
    section.className = 'lista-section';
    const ul = document.createElement('ul');
    ul.className = 'lista-ingredientes';
    ingredientes.forEach(ing => {
      const itemKey = `${slug}::${ing}`;
      const isChecked = !!checked[itemKey];
      const li = document.createElement('li');
      li.className = 'lista-item' + (isChecked ? ' checked' : '');
      li.innerHTML = `<label><input type="checkbox"${isChecked ? ' checked' : ''}><span>${ing}</span></label>`;
      li.querySelector('input').addEventListener('change', e => {
        const c = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        if (e.target.checked) { c[itemKey] = true; li.classList.add('checked'); }
        else { delete c[itemKey]; li.classList.remove('checked'); }
        localStorage.setItem(STORAGE_KEY, JSON.stringify(c));
      });
      ul.appendChild(li);
    });
    section.innerHTML = `<h3>${nome}</h3>`;
    section.appendChild(ul);
    listDiv.appendChild(section);
  });

  if (!hasContent) {
    listDiv.innerHTML = '<p>Não foi possível carregar os ingredientes das receitas selecionadas.</p>';
  }
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
  document.querySelectorAll('.lista-section').forEach(sec => {
    lines.push('\n' + sec.querySelector('h3').textContent);
    sec.querySelectorAll('.lista-item span').forEach(span => lines.push('• ' + span.textContent));
  });
  navigator.clipboard.writeText(lines.join('\n').trim()).then(() => {
    const btn = document.querySelector('[onclick="copiarLista()"]');
    btn.textContent = 'Copiado!';
    setTimeout(() => btn.textContent = 'Copiar lista', 2000);
  });
}

document.addEventListener('DOMContentLoaded', renderSelector);
