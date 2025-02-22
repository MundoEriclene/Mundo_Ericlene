// Função para salvar dados no armazenamento local (localStorage)
function salvarDados(chave, dados) {
  localStorage.setItem(chave, JSON.stringify(dados));
  exibirMensagem('Dados salvos com sucesso!');
}

// Função para carregar dados do armazenamento local
function carregarDados(chave) {
  const dados = localStorage.getItem(chave);
  return dados ? JSON.parse(dados) : null;
}

// Função para exibir mensagens no site
function exibirMensagem(mensagem) {
  const notificacao = document.createElement('div');
  notificacao.className = 'notificacao';
  notificacao.innerText = mensagem;
  document.body.appendChild(notificacao);
  setTimeout(() => notificacao.remove(), 3000);
}

// Função para limpar formulários após envio
function limparFormulario(form) {
  form.reset();
  const seccoes = form.closest('section');
  if (seccoes) seccoes.classList.remove('ativo');
}

// Função para abrir/fechar seções ao clicar no título
function toggleSection(id) {
  const secao = document.getElementById(id);
  secao.classList.toggle('ativo');
}

// Lista de refeições por categoria
const opcoesRefeicoes = {
  "Café da manhã": ["Pão com queijo e fiambre", "Bolacha com sumo", "Iogurte com granola", "Frutas frescas", "Aveia com mel", "Panquecas integrais", "Smoothie de frutas", "Ovos mexidos", "Torradas integrais", "Chá verde"],
  "Almoço": ["Arroz com frango grelhado", "Salada de atum", "Feijoada", "Lasanha de legumes", "Peixe assado", "Bife de peru", "Sopa de legumes", "Espaguete integral", "Estufado de carne", "Salada de quinoa"],
  "Jantar": ["Sopa leve", "Sanduíche natural", "Salada de frango", "Omelete de claras", "Peixe grelhado", "Wrap integral", "Tapioca com queijo", "Caldo verde", "Carne branca grelhada", "Vegetais cozidos"],
  "Lanches": ["Frutas secas", "Nozes", "Barra de cereais", "Iogurte natural", "Biscoito integral", "Mix de sementes", "Batata doce", "Pipoca sem óleo", "Suco natural", "Bolacha de arroz"],
  "Extras": ["Chocolate amargo", "Pedaço de bolo", "Sorvete natural", "Biscoito de aveia", "Chips de batata doce", "Gelatina", "Pão de queijo", "Muffin de banana", "Torrada com abacate", "Frutas cristalizadas"]
};

// Registro de sono
function salvarSono(event) {
  event.preventDefault();
  const horarioDormir = document.getElementById('horarioDormir').value;
  const horarioAcordar = document.getElementById('horarioAcordar').value;
  const qualidadeSono = document.getElementById('qualidadeSono').value;
  const justificativaSono = document.getElementById('justificativaSono').value;

  salvarDados('sono', { horarioDormir, horarioAcordar, qualidadeSono, justificativaSono });
  limparFormulario(event.target);
}

// Registro de alimentação
function carregarOpcoesRefeicao() {
  const refeicaoSelect = document.getElementById('refeicao');
  const opcoesRefeicaoDiv = document.getElementById('opcoesRefeicao');
  const categoria = refeicaoSelect.value;
  const opcoes = opcoesRefeicoes[categoria] || [];
  opcoesRefeicaoDiv.innerHTML = opcoes.map(opcao => `
    <label>
      <input type="checkbox" value="${opcao}" data-calorias="150"> ${opcao}
    </label>`).join('');
  opcoesRefeicaoDiv.style.display = 'block';
}

document.addEventListener('click', (e) => {
  const refeicaoSelect = document.getElementById('refeicao');
  const opcoesRefeicaoDiv = document.getElementById('opcoesRefeicao');
  if (!refeicaoSelect.contains(e.target) && !opcoesRefeicaoDiv.contains(e.target)) {
    opcoesRefeicaoDiv.style.display = 'none';
  }
});

function salvarAlimentacao(event) {
  event.preventDefault();
  const refeicoesSelecionadas = [...document.querySelectorAll('#opcoesRefeicao input:checked')].map(input => input.value);
  const descricaoRefeicao = document.getElementById('descricaoRefeicao').value;
  const calorias = document.getElementById('calorias').value;
  const agua = document.getElementById('agua').value;

  salvarDados('alimentacao', { refeicoesSelecionadas, descricaoRefeicao, calorias, agua });
  limparFormulario(event.target);
  document.getElementById('opcoesRefeicao').innerHTML = '';
}
