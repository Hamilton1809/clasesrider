const  version = '1.2.0';
function saludar(nombre) {
    return `Hola, ${nombre}!`;
}

function healtcheck() {
    return {
        status: 'ok',
        version: version,
        timestamp: new Date().toISOString(),
        message: 'El sistema está funcionando correctamente.'
    };
}

function verificarsistema() {
    const resultado = healtcheck();
    const statusdiv = document.getElementById('status');
    statusdiv.textContent = `${resultado.message} | ${resultado.timestamp}`;
    statusdiv.style.color = '#009b4C';
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('version').textContent = `Versión: ${version}`;
    verificarsistema();
})