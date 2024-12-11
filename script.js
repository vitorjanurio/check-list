async function getDados(tabela) {
    const response = await fetch(`http://127.0.0.1:5000/api/${tabela}`);
    const dados = await response.json();
    console.log(dados); 
  }
  
  
  getDados('funcionario');
  getDados('avaria');
  getDados('retorno');
  