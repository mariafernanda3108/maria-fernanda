const usuarios = [
    {nome: 'Ana', idade: 25},
    {nome: 'Marta', idade: 32},
    {nome: 'Maria', idade: 45} 
]

console.log('Exibindo todos os elementos do vetor.')
usuarios.forEach(usuario => {
    console.log(`${usuario.nome} tem ${usuario.idade} anos.`)
})

console.log('\nFiltrando usuario.')
const menorQueTrintaAnos = usuarios.filter(usuario => usuario.idade <= 30)
menorQueTrintaAnos.forEach(usuario => console.log(`${usuario.nome} tem ${usuario.idade} anos`))

console.log('\nExibindo apenas um nome dos usuarios.')
const nomes = usuarios.map(usuario => usuario.nome)
nomes.forEach(nome => {
    console.log(`Nome: ${nome}`)
})

console.log('\nExibindo o nome dos usuarios com numeracao.')
nomes.forEach( (nome, index) => {
    console.log(`${++index}: ${nome}`)
})

console.log('\nEncontrar um usuario.')
const usuarioEncontrado = usuarios.find(usuario => usuario.nome === 'Marta')
console.log(`Nome: ${usuarioEncontrado.nome}, idade: ${usuarioEncontrado.idade}`)

console.log('\nMostrar a soma de todas as idades.')
const somaIdade = usuarios.reduce((total, usuario) => total + usuario.idade, 0)
console.log(`Total: ${somaIdade}`)