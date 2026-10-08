const tentativas = document.getElementById("tentativa")
let max = Number(prompt('digite o ultimo numero: (bota em numero)'))

console.log(tentativas)
const valorCerto = Math.floor(Math.random() * max) + 1; 
//
let chute = 0;
let tentativa = 1
while (chute != valorCerto) {
    chute = Number(prompt(`chuta o numero de 1 ate ${max}`));
    if (chute > valorCerto) {
        alert("Tente valor menor");
    } else if (chute < valorCerto) {
        alert("Tente  valor maior");
    } else if (chute === valorCerto) {
        alert("Você acertou!");
        tentativas.innerText =`voce acertou com ${tentativa} tentativas`
    } else {
        alert("tenta com numero");
    }
    tentativa++
}

