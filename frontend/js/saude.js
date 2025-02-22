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
  "Café da manhã": ["Pão com queijo e fiambre", "Bolacha com sumo", "Iogurte com granola", "Frutas frescas", "Aveia com mel"],
  "Almoço": ["Arroz com frango grelhado", "Salada de atum", "Feijoada", "Lasanha de legumes", "Peixe assado"],
  "Jantar": ["Sopa leve", "Sanduíche natural", "Salada de frango", "Omelete de claras", "Peixe grelhado"],
  "Lanches": ["Frutas secas", "Nozes", "Barra de cereais", "Iogurte natural", "Biscoito integral"],
  "Extras": ["Chocolate amargo", "Pedaço de bolo", "Sorvete natural", "Biscoito de aveia", "Chips de batata doce"]
};

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

// Função para registrar dados de sono com envio
async function salvarSono(event) {
  event.preventDefault();

  const horarioReal = document.getElementById("horarioReal").value;
  const qualidadeSono = document.getElementById("qualidadeSono").value;
  const justificativaSono = document.getElementById("justificativaSono").value;

  if (!horarioReal || qualidadeSono === "" || justificativaSono.trim() === "") {
    Swal.fire({
      icon: 'error',
      title: 'Campos Incompletos',
      text: 'Por favor, preencha todos os campos.',
    });
    return false;
  }

  const dadosSono = {
    horarioReal,
    qualidadeSono: parseInt(qualidadeSono),
    justificativaSono
  };

  try {
    const response = await fetch("https://mundo-ericlene.onrender.com/saude/sono", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosSono),
    });

    const data = await response.json();

    if (response.ok) {
      Swal.fire({
        icon: 'success',
        title: 'Sucesso!',
        text: 'Seus dados de sono foram salvos com sucesso!',
      });
      limparFormulario(event.target);
    } else {
      Swal.fire({
        icon: 'error',
        title: 'Erro!',
        text: data.message || 'Ocorreu um erro ao salvar os dados.',
      });
    }
  } catch (error) {
    Swal.fire({
      icon: 'error',
      title: 'Erro de Conexão',
      text: 'Não foi possível conectar ao servidor.',
    });
  }
}
