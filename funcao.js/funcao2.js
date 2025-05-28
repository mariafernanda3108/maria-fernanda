// Arrow function
const somar = (a, b) => {
    return a + b
}

//Arrow function
const subtrair = (a, b) => {
    return a - b
}

const multiplicar = (a, b) => {
    return a * b
}

const dividir = (a, b) => {
    return a / b
}

// Chamando uma funcao
const soma = somar(2,3)
const subtracao = subtrair (2, 3)
const multiplicacao = multiplicar (2, 3)
const divisao = dividir (2, 3)
// Exibir resultado.
console.log(`Soma: ${soma}`)
console.log(`Subtrair: ${subtracao}`)
console.log(`multiplicar: ${multiplicacao}`)
console.log(`dividir: ${divisao}`)