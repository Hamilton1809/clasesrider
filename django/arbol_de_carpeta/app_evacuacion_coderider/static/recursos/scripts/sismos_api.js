document.addEventListener('DOMContentLoaded', function() {
    if (typeof URL_API_SISMOS !== 'undefined' && URL_API_SISMOS) {
        fetch(URL_API_SISMOS)
            .then(response => {
                if (!response.ok) throw new Error("Error en la red");
                return response.json();
            })
            .then(data => {
                console.log("Conexión exitosa con API Sismos. Sismos disponibles:", data.features.length);
            })
            .catch(err => console.warn("Aviso al consultar API de sismos:", err.message));
    }
});