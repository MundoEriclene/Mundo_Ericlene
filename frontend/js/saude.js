// Função para salvar dados no armazenamento local (localStorage)
function salvarDados(chave, dados) {
    localStorage.setItem(chave, JSON.stringify(dados));
  }
  
  // Função para carregar dados do armazenamento local
  function carregarDados(chave) {
    const dados = localStorage.getItem(chave);
    return dados ? JSON.parse(dados) : null;
  }
  
  // Registro de sono
  const formSono = document.querySelector('#sono form');
  formSono.addEventListener('submit', (e) => {
    e.preventDefault();
    const horarioDormir = document.getElementById('horarioDormir').value;
    const horarioAcordar = document.getElementById('horarioAcordar').value;
    const qualidadeSono = document.getElementById('qualidadeSono').value;
  
    salvarDados('sono', { horarioDormir, horarioAcordar, qualidadeSono });
    alert('Dados de sono salvos com sucesso!');
  });
  
  // Registro de alimentação
  const formAlimentacao = document.querySelector('#alimentacao form');
  formAlimentacao.addEventListener('submit', (e) => {
    e.preventDefault();
    const calorias = document.getElementById('calorias').value;
    const hidratacao = document.getElementById('hidratacao').value;
  
    salvarDados('alimentacao', { calorias, hidratacao });
    alert('Dados de alimentação salvos com sucesso!');
  });
  
  // Registro de exercícios
  const formExercicios = document.querySelector('#exercicios form');
  formExercicios.addEventListener('submit', (e) => {
    e.preventDefault();
    const tipoExercicio = document.getElementById('tipoExercicio').value;
    const duracaoExercicio = document.getElementById('duracaoExercicio').value;
  
    salvarDados('exercicios', { tipoExercicio, duracaoExercicio });
    alert('Dados de exercícios salvos com sucesso!');
  });
  
  // Registro de higiene pessoal
  const formHigiene = document.querySelector('#higiene form');
  formHigiene.addEventListener('submit', (e) => {
    e.preventDefault();
    const escovacao = document.getElementById('escovacao').checked;
    const banho = document.getElementById('banho').checked;
  
    salvarDados('higiene', { escovacao, banho });
    alert('Dados de higiene pessoal salvos com sucesso!');
  });
  
  // Função de notificação push
  function solicitarPermissaoNotificacao() {
    if ('Notification' in window) {
      Notification.requestPermission().then((permissao) => {
        if (permissao === 'granted') {
          enviarNotificacao('Bem-vindo ao Mundo Ericlene!');
        }
      });
    }
  }
  
  function enviarNotificacao(mensagem) {
    if (Notification.permission === 'granted') {
      new Notification(mensagem);
    }
  }
  
  // Ativando notificação ao carregar a página
  window.onload = () => {
    solicitarPermissaoNotificacao();
    carregarDadosPreenchidos();
  };
  
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
      document.getElementById('calorias').value = alimentacao.calorias;
      document.getElementById('hidratacao').value = alimentacao.hidratacao;
    }
  
    const exercicios = carregarDados('exercicios');
    if (exercicios) {
      document.getElementById('tipoExercicio').value = exercicios.tipoExercicio;
      document.getElementById('duracaoExercicio').value = exercicios.duracaoExercicio;
    }
  
    const higiene = carregarDados('higiene');
    if (higiene) {
      document.getElementById('escovacao').checked = higiene.escovacao;
      document.getElementById('banho').checked = higiene.banho;
    }
  }
  