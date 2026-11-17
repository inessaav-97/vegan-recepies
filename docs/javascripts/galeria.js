const RECEITAS = [
  { nome: 'Arroz de Abóbora, Cogumelos e Romã', img: '388d67a5-823f-4b47-890d-8a3a2f251235.jpg', slug: 'arroz-abobora-cogumelos-roma' },
  { nome: 'Arroz Salteado Oriental com Tofu e Cajus', img: 'arroz-oriental.jpeg', slug: 'arroz-salteado-tofu-cajus' },
  { nome: 'Barcos de Curgete Pizza', img: 'zucchini-pizza.jpg', slug: 'barcos-de-curgete-pizza' },
  { nome: 'Batata Doce Recheada com Grão-de-Bico', img: 'batata-doce-recheada.jpeg', slug: 'batata-doce-recheada' },
  { nome: 'Bifes de Couve-flor Panados', img: 'cauliflower-steaks-recipe.jpg', slug: 'bifes-de-couve-flor-panados' },
  { nome: 'Biryani de Tofu Vegano', img: '6cfc37ab-0ec4-4b9c-84ec-8cca6208f2f9.jpg', slug: 'biryani-tofu-vegano' },
  { nome: 'Bowl de Edamame com Arroz de Sushi', img: 'bowl-edamame-sushi.jpeg', slug: 'bowl-edamame-sushi' },
  { nome: 'Caril de Beringela e Lentilhas com Coco e Damasco', img: '1bb509ae-a1b9-4aeb-b05f-8959f3565133.jpg', slug: 'caril-beringela-lentilhas' },
  { nome: 'Caril Massaman', img: 'massaman-curry.jpg', slug: 'caril-massaman' },
  { nome: 'Chow Mein', img: 'chow-mein.jpg', slug: 'chow-mein' },
  { nome: 'Esparguete com Pesto de Tofu', img: '', slug: 'esparguete-pesto-tofu' },
  { nome: 'Estrogonofe de Grão-de-Bico', img: 'ec937e3d-bb1c-4847-a988-3ce85a7a0f1b.jpg', slug: 'estrogonofe-grao-de-bico' },
  { nome: 'Feijocas com Leite de Coco e Espinafres', img: 'feijocas-leite-coco-espinafres.jpeg', slug: 'feijocas-leite-coco-espinafres' },
  { nome: 'Feijões Brancos Cremosos à Toscana', img: 'ddc02ce2-e43a-4c98-8d83-5967f5a1a111.jpg', slug: 'feijoes-brancos-toscana' },
  { nome: 'Feijões com Miso, Tahine e Sementes Tostadas', img: '957111ee-9a99-4163-920f-343279b12236.jpg', slug: 'feijoes-miso-verde' },
  { nome: 'Filetes de Tofu à Russa', img: '3f3372fc-1348-40a5-8a37-ecc3bd8c7ecd.jpg', slug: 'filetes-tofu-russos' },
  { nome: 'Gnocchi com Creme de Castanha e Tomates', img: 'Gnocchi-tomates.jpeg', slug: 'gnocchi-creme-castanha-tomates' },
  { nome: 'Gnocchi com Tomates, Lentilhas e Tofu', img: '', slug: 'gnocchi-tomates-lentilhas' },
  { nome: 'Gnocchi Cremoso com Abóbora', img: '662977a6-8e27-4ba1-8531-cae9e2ab503d.jpg', slug: 'gnocchi-cremoso-abobora' },
  { nome: 'Lentilhas Cremosas com Espinafre', img: '', slug: 'lentilhas-cremosas-espinafre' },
  { nome: 'Massa al Ragù Vegano', img: '903712fc-173d-4c2a-9536-6f2388e90607.jpg', slug: 'massa-ragu-vegano' },
  { nome: 'Massa com Pimento Vermelho Assado', img: 'roasted-red-pepper-and-vegetable-pasta.jpg', slug: 'massa-com-pimento-vermelho-assado' },
  { nome: 'Massa Cremosa com Cogumelos e Miso', img: '', slug: 'massa-cogumelos-miso' },
  { nome: 'Massa Cremosa de Pimento Vermelho Assado', img: '6bef5146-8794-44de-a061-3d4ac43813e5.jpg', slug: 'massa-pimento-cremosa' },
  { nome: 'Massa de Alta Proteína', img: 'e9afd5b4-5ed5-41d9-90ac-a2e338b74461.jpg', slug: 'massa-alta-proteina' },
  { nome: 'Nachos com Feijão Preto e Guacamole', img: 'nachos-feijao-preto.jpeg', slug: 'nachos-feijao-preto' },
  { nome: 'Noodles de Curry com Leite de Coco', img: '82e59aa2-ba35-49ab-930d-49fa6b86471d.jpg', slug: 'noodles-curry-coco' },
  { nome: 'Orzo com Tomates Secos e Tofu', img: '', slug: 'orzo-tomates-secos-tofu' },
  { nome: 'Queques de Tofu com Tomate Seco', img: 'queques-tofu-tomate-seco.jpeg', slug: 'queques-tofu-tomate-seco' },
  { nome: 'Quiche de Batata com Tofu e Legumes', img: 'quiche-batata-tofu.jpeg', slug: 'quiche-batata-tofu' },
  { nome: 'Ramen de Legumes', img: 'veggie-ramen-recipe.jpg', slug: 'ramen-de-legumes' },
  { nome: 'Salada de Falafel no Forno', img: 'baked-falafel-salad.jpg', slug: 'salada-de-falafel-no-forno' },
  { nome: 'Salada Nutritiva com Molho de Tahine', img: 'b0f09471-f3f3-4b56-964f-caadbcad2bef.jpg', slug: 'salada-molho-tahine' },
  { nome: 'Shawarma de Cogumelos', img: 'mushroom-shawarma.jpg', slug: 'shawarma-de-cogumelos' },
  { nome: 'Tofu com Beringela Assada', img: '3f9d972d-a5dc-4d6c-a384-bf39f4bc9514.jpg', slug: 'tofu-beringela-assada' },
  { nome: 'Tofu com Molho de Laranja', img: '9a252c26-b806-427c-8861-8754669b41ac.jpg', slug: 'tofu-laranja' },
  { nome: 'Tofu com Sésamo e Brócolos', img: 'tofu-sesamo-broculos.jpeg', slug: 'tofu-sesamo-broculos' },
  { nome: 'Tofu Salteado com Legumes', img: 'chop-suey-vegan.jpeg', slug: 'tofu-salteado-legumes' },
  { nome: 'Udon Cremoso com Tofu', img: '', slug: 'udon-cremoso-tofu' },
  { nome: 'Wellington Vegano', img: '6851fed3-5d46-4091-9741-69c25b44f199.jpg', slug: 'wellington-vegano' },
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
