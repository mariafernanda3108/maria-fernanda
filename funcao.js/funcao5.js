// criando uma lista.
const numeros = [1, 2, 3, 4, 5]

console.log('Exibindo elementos da lista.')
console.log(numeros)

console.log('\nMultiplicacao com elementos da lista.')
const dobrados = numeros.map(n => n * 2)
console.log(dobrados)

console.log('\nFiltrando numeros pares.')
const pares = numeros.filter(n => n % 2 === 0)
console.log(pares)

console.log('\nSomando todos os numeros do vetor.')
const total = numeros.reduce((soma, atual) => soma + atual, 0)
console.log(total)

