 function gerarBotao() {
    const idadeInput = document.getElementById('idadeInput');
    const idade = parseInt(idadeInput.value);
    
    const resultadoDoiv = document.getElementById('resultado');
    resultadoDiv.innerHTML = ''; // limpar resultado anterior

