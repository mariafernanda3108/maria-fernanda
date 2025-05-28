// criando um vetor.
const frutas = ['maca' , 'banana', 'laranja']

console.log('Exibindo todos os elemntos dentro do vetor.')


console.log('Exibindo apenas um elemntos dentro do vetor.')
console.log(frutas[0])
console.log(frutas[2])

console.log('\nAdicionando elemento ao vetor.')
frutas.push('uvas')
console.log(frutas)

console.log('\nRemovendo o ultimo elemento do vetor.')
frutas.pop()
console.log(frutas)

console.log('\nRemovendoo o primeiro elemento do vetor.')
frutas.shift()
console.log(frutas)

console.log('\nPercorrendo o vetor.')
frutas.forEach((fruta, index) => {
    console.log(`${++index}: ${fruta}`)
})
