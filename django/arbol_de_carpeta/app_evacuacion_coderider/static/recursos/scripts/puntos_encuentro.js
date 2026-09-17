document.addEventListener('DOMContentLoaded', function() {
    var btnPuntos = document.getElementById('btn-mostrar-punto');
    var containerPuntos = document.getElementById('lista-puntos');
    var mapPuntos = null;

    if (btnPuntos && containerPuntos) {
        btnPuntos.addEventListener('click', function() {
            if (!mapPuntos) {
                mapPuntos = L.map('lista-puntos').setView([2.4419, -76.6063], 14);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19,
                    attribution: '&copy; OpenStreetMap'
                }).addTo(mapPuntos);

                if (typeof URL_JSON !== 'undefined' && URL_JSON) {
                    fetch(URL_JSON)
                        .then(res => res.json())
                        .then(puntos => {
                            puntos.forEach(p => {
                                if (p.lat && p.lng) {
                                    L.marker([p.lat, p.lng]).addTo(mapPuntos)
                                        .bindPopup(`<b>${p.nombre || 'Punto de Encuentro'}</b><br>${p.descripcion || ''}`);
                                }
                            });
                        })
                        .catch(err => console.log("Aviso: No se cargaron puntos JSON."));
                }
            }

            setTimeout(function() { 
                if (mapPuntos) mapPuntos.invalidateSize(); 
            }, 200);
        });
    }
});