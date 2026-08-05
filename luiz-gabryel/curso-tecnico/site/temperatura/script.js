function temperatura() {
    let valor = Number(document.getElementById("temperatura").valor);
    let mensagem = document.getElementById("mensagem");

    if (valor > 38) {
        mensagem.innerHTML = "eita calor do caralho";
    } else if (valor < 30) {
        mensagem.innerHTML = "frio";
    } else {
        mensagem.innerHTML = "normal";
    }
}
