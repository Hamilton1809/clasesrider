// Importación moderna (Requiere type="module" en el HTML)
import estilosNuevos from './componentes.css' with { type: 'css' };
document.adoptedStyleSheets = [...document.adoptedStyleSheets, estilosNuevos];

// Control del menú móvil
document.querySelectorAll('.nav-item').forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    });
});