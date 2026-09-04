function toStem(word) {
  return word.endsWith('s') ? word.slice(0, -1) : word;
}

function matchesIngredient(text, ingredient) {
  const stem = toStem(ingredient);
  const regex = new RegExp(stem + 's?\\b', 'i');
  return regex.test(text);
}

async function searchIngredients() {
  const input = document.getElementById('ingredient-input').value;
  const ingredients = input.split(',').map(i => i.trim().toLowerCase()).filter(i => i);
  const resultsDiv = document.getElementById('search-results');

  if (ingredients.length === 0) {
    resultsDiv.innerHTML = '<p>Escreve pelo menos um ingrediente.</p>';
    return;
  }

  try {
    const response = await fetch('../search/search_index.json');
    const data = await response.json();

    // Group all sections by base page location
    const pages = {};
    for (const doc of data.docs) {
      const loc = doc.location.split('#')[0];
      if (!loc.match(/pratos-principais|sopas|sobremesas/)) continue;

      if (!pages[loc]) pages[loc] = { title: '', text: '', href: '../' + loc };

      // Only use title from the main page entry (no anchor)
      if (!doc.location.includes('#')) pages[loc].title = doc.title;

      pages[loc].text += ' ' + doc.title + ' ' + doc.text;
    }

    const results = Object.values(pages).filter(page =>
      ingredients.every(ing => matchesIngredient(page.text.toLowerCase(), ing))
    );

    if (results.length === 0) {
      resultsDiv.innerHTML = `<p>Nenhuma receita encontrada com: <strong>${ingredients.join(', ')}</strong>.</p>`;
    } else {
      resultsDiv.innerHTML = `<ul>${results.map(r => `<li><a href="${r.href}">${r.title}</a></li>`).join('')}</ul>`;
    }
  } catch (e) {
    resultsDiv.innerHTML = '<p>Erro ao carregar receitas. Tenta novamente.</p>';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('ingredient-input');
  if (input) {
    input.addEventListener('keydown', e => {
      if (e.key === 'Enter') searchIngredients();
    });
  }
});
