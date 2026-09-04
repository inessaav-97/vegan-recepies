function getKey() {
  return 'rating_' + window.location.pathname;
}

function renderStars(container, saved) {
  container.innerHTML = '';
  const wrapper = document.createElement('div');
  wrapper.className = 'star-rating' + (saved ? ' locked' : '');

  const label = document.createElement('span');
  label.className = 'star-label';
  label.textContent = saved ? `A tua classificação: ${saved}/5` : 'Classifica esta receita:';
  wrapper.appendChild(label);

  const stars = [];
  for (let i = 1; i <= 5; i++) {
    const s = document.createElement('span');
    s.className = 'star' + (saved && i <= saved ? ' active' : '');
    s.textContent = '★';
    s.dataset.value = i;
    stars.push(s);
    wrapper.appendChild(s);
  }

  if (!saved) {
    stars.forEach(s => {
      s.addEventListener('mouseover', () => {
        const v = +s.dataset.value;
        stars.forEach(x => x.classList.toggle('hover', +x.dataset.value <= v));
      });
      s.addEventListener('mouseout', () => stars.forEach(x => x.classList.remove('hover')));
      s.addEventListener('click', () => {
        localStorage.setItem(getKey(), s.dataset.value);
        renderStars(container, +s.dataset.value);
      });
    });
  }

  container.appendChild(wrapper);
}

document.addEventListener('DOMContentLoaded', () => {
  // Only run on individual recipe pages, not section indexes
  const path = window.location.pathname;
  if (!path.match(/\/(pratos-principais|sopas|sobremesas)\/[^/]+\//)) return;

  const saved = +localStorage.getItem(getKey()) || null;
  const container = document.createElement('div');
  container.id = 'star-rating-container';
  renderStars(container, saved);

  const img = document.querySelector('.md-content__inner img');
  const h1 = document.querySelector('.md-content__inner h1');
  if (img) img.insertAdjacentElement('afterend', container);
  else if (h1) h1.insertAdjacentElement('afterend', container);
});
