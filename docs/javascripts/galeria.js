const RECEITAS = [
  { nome: 'Arroz Salteado Oriental com Tofu e Cajus', img: 'arroz-oriental.jpeg', slug: 'arroz-salteado-tofu-cajus' },
  { nome: 'Barcos de Curgete Pizza', img: 'zucchini-pizza.jpg', slug: 'barcos-de-curgete-pizza' },
  { nome: 'Bifes de Couve-flor Panados', img: 'cauliflower-steaks-recipe.jpg', slug: 'bifes-de-couve-flor-panados' },
  { nome: 'Bowl de Edamame com Arroz de Sushi', img: 'bowl-edamame-sushi.jpeg', slug: 'bowl-edamame-sushi' },
  { nome: 'Caril Massaman', img: 'massaman-curry.jpeg', slug: 'caril-massaman' },
  { nome: 'Chow Mein', img: 'chow-mein.jpg', slug: 'chow-mein' },
  { nome: 'Esparguete com Pesto de Tofu', img: '', slug: 'esparguete-pesto-tofu' },
  { nome: 'Feijocas com Leite de Coco e Espinafres', img: 'feijocas-leite-coco-espinafres.jpeg', slug: 'feijocas-leite-coco-espinafres' },
  { nome: 'Gnocchi com Creme de Castanha e Tomates', img: '', slug: 'gnocchi-creme-castanha-tomates' },
  { nome: 'Gnocchi com Tomates, Lentilhas e Tofu', img: '', slug: 'gnocchi-tomates-lentilhas' },
  { nome: 'Lentilhas Cremosas com Espinafre', img: '', slug: 'lentilhas-cremosas-espinafre' },
  { nome: 'Massa com Pimento Vermelho Assado', img: 'roasted-red-pepper-and-vegetable-pasta.jpg', slug: 'massa-com-pimento-vermelho-assado' },
  { nome: 'Massa Cremosa com Cogumelos e Miso', img: '', slug: 'massa-cogumelos-miso' },
  { nome: 'Nachos com Feijão Preto e Guacamole', img: 'nachos-feijao-preto.jpeg', slug: 'nachos-feijao-preto' },
  { nome: 'Orzo com Tomates Secos e Tofu', img: '', slug: 'orzo-tomates-secos-tofu' },
  { nome: 'Queques de Tofu com Tomate Seco', img: 'queques-tofu-tomate-seco.jpeg', slug: 'queques-tofu-tomate-seco' },
  { nome: 'Quiche de Batata com Tofu e Legumes', img: 'quiche-batata-tofu.jpeg', slug: 'quiche-batata-tofu' },
  { nome: 'Ramen de Legumes', img: 'veggie-ramen-recipe.jpg', slug: 'ramen-de-legumes' },
  { nome: 'Salada de Falafel no Forno', img: 'baked-falafel-salad.jpg', slug: 'salada-de-falafel-no-forno' },
  { nome: 'Shawarma de Cogumelos', img: 'mushroom-shawarma.jpeg', slug: 'shawarma-de-cogumelos' },
  { nome: 'Tofu com Sésamo e Brócolos', img: 'tofu-sesamo-broculos.jpeg', slug: 'tofu-sesamo-broculos' },
  { nome: 'Tofu Salteado com Legumes', img: 'chop-suey-vegan.jpeg', slug: 'tofu-salteado-legumes' },
  { nome: 'Udon Cremoso com Tofu', img: '', slug: 'udon-cremoso-tofu' },
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
        ${r.img ? `<img src="../imagens/${r.img}" alt="${r.nome}" loading="lazy" onerror="this.style.display='none'">` : ''}
      </div>
      <span class="recipe-card-name">${r.nome}</span>
    `;
    grid.appendChild(card);
  });

  container.appendChild(grid);
});
