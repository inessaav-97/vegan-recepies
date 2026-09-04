const RECEITAS = [
  { nome: 'Arroz Salteado Oriental com Tofu e Cajus', slug: 'arroz-salteado-tofu-cajus' },
  { nome: 'Barcos de Curgete Pizza', slug: 'barcos-de-curgete-pizza' },
  { nome: 'Bifes de Couve-flor Panados', slug: 'bifes-de-couve-flor-panados' },
  { nome: 'Bowl de Edamame com Arroz de Sushi', slug: 'bowl-edamame-sushi' },
  { nome: 'Caril Massaman', slug: 'caril-massaman' },
  { nome: 'Chow Mein', slug: 'chow-mein' },
  { nome: 'Esparguete com Pesto de Tofu', slug: 'esparguete-pesto-tofu' },
  { nome: 'Feijocas com Leite de Coco e Espinafres', slug: 'feijocas-leite-coco-espinafres' },
  { nome: 'Gnocchi com Creme de Castanha e Tomates', slug: 'gnocchi-creme-castanha-tomates' },
  { nome: 'Gnocchi com Tomates, Lentilhas e Tofu', slug: 'gnocchi-tomates-lentilhas' },
  { nome: 'Lentilhas Cremosas com Espinafre', slug: 'lentilhas-cremosas-espinafre' },
  { nome: 'Massa com Pimento Vermelho Assado', slug: 'massa-com-pimento-vermelho-assado' },
  { nome: 'Massa Cremosa com Cogumelos e Miso', slug: 'massa-cogumelos-miso' },
  { nome: 'Nachos com Feijão Preto e Guacamole', slug: 'nachos-feijao-preto' },
  { nome: 'Orzo com Tomates Secos e Tofu', slug: 'orzo-tomates-secos-tofu' },
  { nome: 'Queques de Tofu com Tomate Seco', slug: 'queques-tofu-tomate-seco' },
  { nome: 'Quiche de Batata com Tofu e Legumes', slug: 'quiche-batata-tofu' },
  { nome: 'Ramen de Legumes', slug: 'ramen-de-legumes' },
  { nome: 'Salada de Falafel no Forno', slug: 'salada-de-falafel-no-forno' },
  { nome: 'Shawarma de Cogumelos', slug: 'shawarma-de-cogumelos' },
  { nome: 'Tofu com Sésamo e Brócolos', slug: 'tofu-sesamo-broculos' },
  { nome: 'Tofu Salteado com Legumes', slug: 'tofu-salteado-legumes' },
  { nome: 'Udon Cremoso com Tofu', slug: 'udon-cremoso-tofu' },
];

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('recipe-gallery');
  if (!container) return;

  const grid = document.createElement('div');
  grid.className = 'recipe-gallery';

  RECEITAS.forEach(r => {
    const card = document.createElement('a');
    card.className = 'recipe-card';
    card.href = r.slug + '/';
    card.innerHTML = `
      <div class="recipe-card-img">
        <img src="../imagens/${r.slug}.jpg" alt="${r.nome}" loading="lazy" onerror="this.style.display='none'">
      </div>
      <span class="recipe-card-name">${r.nome}</span>
    `;
    grid.appendChild(card);
  });

  container.appendChild(grid);
});
