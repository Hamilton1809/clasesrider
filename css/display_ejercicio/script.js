// Seleccionamos los 9 cuadros de la pantalla
const cuadros = document.querySelectorAll('.cuadro');

cuadros.forEach(cuadro => {
    let temporizador = null;

    // --- ACCIÓN PARA 1 CLIC ---
    cuadro.addEventListener('click', () => {
        // Si no hay un temporizador activo, iniciamos uno
        if (!temporizador) {
            temporizador = setTimeout(() => {
                // Si pasa un cuarto de segundo y no hiciste otro clic:
                cuadro.style.display = 'none'; // SE QUITA POR COMPLETO
                temporizador = null;
            }, 250); // Tiempo de espera (250 milisegundos)
        }
    });

    // --- ACCIÓN PARA 2 CLICS (Doble clic) ---
    cuadro.addEventListener('dblclick', () => {
        // Cancelamos la orden del primer clic para que no se borre del todo
        clearTimeout(temporizador);
        temporizador = null;

        // Ocultamos el cuadro pero conservamos su espacio en blanco
        cuadro.style.visibility = 'hidden'; // SE OCULTA PERO DEJA EL HUECO
    });
});