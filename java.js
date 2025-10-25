// Pega a variável que vem do HTTP
const arr = {{consulta_cotacao}} || [];

// Converte cada string JSON em objeto real
const itens = arr.map(i => JSON.parse(i));

// Monta as linhas do relatório
const linhas = itens.map(item => {
  const valorNum = Number(item.valor_total);
  const valorFormat = valorNum.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  return `${item.quantidade}\t${item.produto_marca}\tR$ ${valorFormat}`;
});

// Soma o total
const total = itens.reduce((acc, item) => acc + Number(item.valor_total), 0);
const totalFormat = total.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

// Salva para usar no bloco de mensagem
setVariable("lista_produtos", linhas.join("\n"));
setVariable("total_cotacao", totalFormat);
setVariable("produtos_json", itens);



// --- Gera lista formatada de produtos e preços ---

const referencia = ["1", "2587", "3698"];
const produto = ["Sobrecoxa Sadia 3Kg", "Mortadela Ouro Perdigão", "Mussarela 3k Seara"];
const preco = ["50.00000000", "80.00000000", "125.36000000"];

let linhas = [];

for (let i = 0; i < referencia.length; i++) {
  const precoNum = parseFloat(preco[i]);
  const precoFormatado = precoNum.toFixed(2).replace('.', ',');
  const linha = `${referencia[i]} ${produto[i]} R$ ${precoFormatado}`;
  linhas.push(linha);



}


// --- Gera lista formatada de produtos e preços ---

const referencia = ["1", "2587", "3698"];
const produto = ["Sobrecoxa Sadia 3Kg", "Mortadela Ouro Perdigão", "Mussarela 3k Seara"];
const preco = ["50.00000000", "80.00000000", "125.36000000"];

let linhas = [];

for (let i = 0; i < referencia.length; i++) {
  const precoNum = parseFloat(preco[i]);
  const precoFormatado = precoNum.toFixed(2).replace('.', ',');
  const linha = `${referencia[i]} ${produto[i]} R$ ${precoFormatado}`;
  linhas.push(linha);
}

const saida = linhas.join("\n");

// 🔹 Define a variável 'saida' para o fluxo do Typebot
setVariable("saida", saida);





// Junta todas as linhas com quebras de linha
const saida = linhas.join("\n");

// Retorna o valor para o Typebot
setVariable(saida);


const arr = {{consulta_cotacao}} || [];

// Monta um array de strings com: "Qtde - Produto - R$ valor"
const nomes = arr.map(i => {
  const item = JSON.parse(i);
//  const valor = Number(item.valor_total).toLocaleString('pt-BR', {
//    minimumFractionDigits: 2,
//    maximumFractionDigits: 2
//  });
//  return `${item.quantidade}  ${item.produto_marca}  R$ ${valor}`;
  return `${item.quantidade} ${item.produto_marca}`;
});

setVariable("lista_nomes", nomes);