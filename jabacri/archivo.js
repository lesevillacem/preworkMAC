const palabras = ["JAVASCRIPT", "AHORCADO", "PROGRAMAR", "BOOTSTRAP", "HTML", "CSS"];
let palabraSecreta = "";
let palabraAdivinada = [];
let intentosRestantes = 6;
let letrasUsadas = [];

function iniciarJuego() {
  // Elegir palabra aleatoria
  palabraSecreta = palabras[Math.floor(Math.random() * palabras.length)];
  palabraAdivinada = Array(palabraSecreta.length).fill("_");
  intentosRestantes = 6;
  letrasUsadas = [];

  document.getElementById("palabra").textContent = palabraAdivinada.join(" ");
  document.getElementById("intentos").textContent = intentosRestantes;
  document.getElementById("letrasUsadas").textContent = "";
  document.getElementById("mensaje").textContent = "";
}

function adivinarLetra() {
  const input = document.getElementById("letra");
  const letra = input.value.toUpperCase();

  if (!letra.match(/[A-ZÑ]/) || letra.length !== 1) {
    alert("Por favor ingresa una letra válida");
    return;
  }

  if (letrasUsadas.includes(letra)) {
    alert("Ya usaste esa letra");
    return;
  }

  letrasUsadas.push(letra);
  document.getElementById("letrasUsadas").textContent = letrasUsadas.join(", ");

  if (palabraSecreta.includes(letra)) {
    for (let i = 0; i < palabraSecreta.length; i++) {
      if (palabraSecreta[i] === letra) {
        palabraAdivinada[i] = letra;
      }
    }
    document.getElementById("palabra").textContent = palabraAdivinada.join(" ");
  } else {
    intentosRestantes--;
    document.getElementById("intentos").textContent = intentosRestantes;
  }

  // Verificar estado del juego
  if (!palabraAdivinada.includes("_")) {
    document.getElementById("mensaje").textContent = "🎉 ¡Ganaste! La palabra era: " + palabraSecreta;
  } else if (intentosRestantes <= 0) {
    document.getElementById("mensaje").textContent = "💀 ¡Perdiste! La palabra era: " + palabraSecreta;
  }

  input.value = "";
}

function reiniciarJuego() {
  iniciarJuego();
}

// Inicializa al cargar
iniciarJuego();
