const palavrasBloqueadas = ["porra", "caralho", "puta"];

function contemPalavraOfensiva(texto) {
    return palavrasBloqueadas.some(palavra => 
        new RegExp(`\\b${palavra}\\b`, 'i').test(texto)
    );
}

document.getElementById("formComentario").onsubmit = function(event) {
    const comentario = document.getElementById("comentario").value;
    if (contemPalavraOfensiva(comentario)) {
        alert("Comentário bloqueado: contém palavras ofensivas.");
        event.preventDefault(); // Impede o envio do comentário
    }
};