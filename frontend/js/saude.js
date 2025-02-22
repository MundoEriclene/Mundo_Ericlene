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

// Lista de refeições por categoria
const opcoesRefeicoes = {
  "Café da manhã": ["Pão com queijo e fiambre", "Bolacha com sumo", "Iogurte com granola", "Frutas frescas", "Aveia com mel", "Panquecas integrais", "Smoothie de frutas", "Ovos mexidos", "Torradas integrais", "Chá verde"],
  "Almoço": ["Arroz com frango grelhado", "Salada de atum", "Feijoada", "Lasanha de legumes", "Peixe assado", "Bife de peru", "Sopa de legumes", "Espaguete integral", "Estufado de carne", "Salada de quinoa"],
  "Jantar": ["Sopa leve", "Sanduíche natural", "Salada de frango", "Omelete de claras", "Peixe grelhado", "Wrap integral", "Tapioca com queijo", "Caldo verde", "Carne branca grelhada", "Vegetais cozidos"],
  "Lanches": ["Frutas secas", "Nozes", "Barra de cereais", "Iogurte natural", "Biscoito integral", "Mix de sementes", "Batata doce", "Pipoca sem óleo", "Suco natural", "Bolacha de arroz"],
  "Extras": ["Chocolate amargo", "Pedaço de bolo", "Sorvete natural", "Biscoito de aveia", "Chips de batata doce", "Gelatina", "Pão de queijo", "Muffin de banana", "Torrada com abacate", "Frutas cristalizadas"]
};

// Registro de sono
const formSono = document.querySelector('#sono form');
formSono.addEventListener('submit', (e) => {
  e.preventDefault();
  const horarioDormir = document.getElementById('horarioDormir').value;
  const horarioAcordar = document.getElementById('horarioAcordar').value;
  const qualidadeSono = document.getElementById('qualidadeSono').value;

  salvarDados('sono', { horarioDormir, horarioAcordar, qualidadeSono });
  limparFormulario(formSono);
});

// Registro de alimentação
const formAlimentacao = document.querySelector('#alimentacao form');
const refeicaoSelect = document.getElementById('refeicao');
const opcoesRefeicaoDiv = document.getElementById('opcoesRefeicao');
const caloriasInput = document.getElementById('calorias');

refeicaoSelect.addEventListener('change', () => {
  const categoria = refeicaoSelect.value;
  const opcoes = opcoesRefeicoes[categoria] || [];
  opcoesRefeicaoDiv.innerHTML = opcoes.map(opcao => `
    <label>
      <input type="checkbox" value="${opcao}" data-calorias="150"> ${opcao}
    </label>`).join('');
});

opcoesRefeicaoDiv.addEventListener('change', () => {
  let totalCalorias = 0;
  opcoesRefeicaoDiv.querySelectorAll('input:checked').forEach(input => {
    totalCalorias += parseInt(input.getAttribute('data-calorias'));
  });
  caloriasInput.value = totalCalorias;
});

formAlimentacao.addEventListener('submit', (e) => {
  e.preventDefault();
  const refeicoesSelecionadas = [...opcoesRefeicaoDiv.querySelectorAll('input:checked')].map(input => input.value);
  const calorias = caloriasInput.value;
  const agua = document.getElementById('agua').value;

  salvarDados('alimentacao', { refeicoesSelecionadas, calorias, agua });
  limparFormulario(formAlimentacao);
  opcoesRefeicaoDiv.innerHTML = '';
});

// Registro de exercícios
const formExercicios = document.querySelector('#exercicios form');
const tipoExercicioSelect = document.getElementById('tipoExercicio');
const duracaoExercicioInput = document.getElementById('duracaoExercicio');

// Sugestão de duração para o exercício
const sugestoes = {
  fisico: 30,
  mental: 15,
  emocional: 20
};

tipoExercicioSelect.addEventListener('change', () => {
  const tipo = tipoExercicioSelect.value;
  duracaoExercicioInput.value = sugestoes[tipo] || 0;
});

formExercicios.addEventListener('submit', (e) => {
  e.preventDefault();
  const tipoExercicio = tipoExercicioSelect.value;
  const duracaoExercicio = duracaoExercicioInput.value;
  const realizado = document.getElementById('realizado').value;

  salvarDados('exercicios', { tipoExercicio, duracaoExercicio, realizado });
  limparFormulario(formExercicios);
});

// Registro de higiene pessoal
const formHigiene = document.querySelector('#higiene form');
formHigiene.addEventListener('submit', (e) => {
  e.preventDefault();
  const higieneDados = {};
  formHigiene.querySelectorAll('input[type="checkbox"]').forEach((input) => {
    higieneDados[input.id] = input.checked;
  });
  salvarDados('higiene', higieneDados);
  limparFormulario(formHigiene);
});

// Carregar dados preenchidos anteriormente
function carregarDadosPreenchidos() {
  const sono = carregarDados('sono');
  if (sono) {
    document.getElementById('horarioDormir').value = sono.horarioDormir;
    document.getElementById('horarioAcordar').value = sono.horarioAcordar;
    document.getElementById('qualidadeSono').value = sono.qualidadeSono;
  }

  const alimentacao = carregarDados('alimentacao');
  if (alimentacao) {
    alimentacao.refeicoesSelecionadas.forEach(refeicao => {
      const checkbox = [...opcoesRefeicaoDiv.querySelectorAll('input')].find(input => input.value === refeicao);
      if (checkbox) checkbox.checked = true;
    });
    caloriasInput.value = alimentacao.calorias;
    document.getElementById('agua').value = alimentacao.agua;
  }

  const exercicios = carregarDados('exercicios');
  if (exercicios) {
    tipoExercicioSelect.value = exercicios.tipoExercicio;
    duracaoExercicioInput.value = exercicios.duracaoExercicio;
    document.getElementById('realizado').value = exercicios.realizado;
  }

  const higiene = carregarDados('higiene');
  if (higiene) {
    for (const key in higiene) {
      document.getElementById(key).checked = higiene[key];
    }
  }
}

window.onload = carregarDadosPreenchidos;
