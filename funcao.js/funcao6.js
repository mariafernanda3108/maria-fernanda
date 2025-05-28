const readlineSync = require ('readline-sync')

let idade;
idade = parseInt(readlineSync.question('Digite sua idade: '))

    if (idade < 16) {
        console.log ('Não pode votar')
        }
    else if (idade === 16 && idade <= 17) {
        console.log ('Voto opcional')
        }
    else if (idade >= 18) {
        console.log ('Voto obrigatório')
        } 
    else (idade >= 65); {
        console.log ('Voto opcional')
    };


