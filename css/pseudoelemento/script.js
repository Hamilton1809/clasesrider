document.getElementById('btn-transicion').addEventListener('click', () => {
    // Verificamos si el navegador soporta View Transitions
    if (!document.startViewTransition) {
        alert("Tu navegador no soporta View Transitions");
        return;
    }

    // Ejecutamos la transición
    document.startViewTransition(() => {
        const caja = document.getElementById('caja-transicion');
        // Cambiamos algo en el DOM
        caja.style.backgroundColor = caja.style.backgroundColor === 'lightblue' ? 'white' : 'lightblue';
    });
});
const modal = document.getElementById('mi-modal');
const btnAbrir = document.getElementById('btn-modal');
const btnCerrar = document.getElementById('btn-cerrar');

// Abrir el modal
btnAbrir.addEventListener('click', () => {
    modal.showModal(); // Esto activa el ::backdrop automáticamente
});

// Cerrar el modal
btnCerrar.addEventListener('click', () => {
    modal.close();
});
document.addEventListener('DOMContentLoaded', () => {
    const card = document.querySelector('.luxury-card');
    const elements = {
        name: document.querySelector('.name'),
        nickname: document.querySelector('.nickname'),
        age: document.querySelector('.age'),
        status: document.querySelector('.status')
    };

    // Mapeo de datos del contenedor hacia los pseudo-elementos
    elements.name.setAttribute('data-name', card.dataset.name);
    elements.nickname.setAttribute('data-nickname', card.dataset.nickname);
    elements.age.setAttribute('data-age', card.dataset.age);
    elements.status.setAttribute('data-status', card.dataset.status);
});