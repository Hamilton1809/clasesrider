// Capa global para agrupar los sismos
let capaSismos = L.layerGroup();

function verSismos() {
    // Detecta cómo se llama tu variable del mapa en mapa.js ('mapa' o 'map')
    const elMapa = (typeof mapa !== 'undefined') ? mapa : (typeof map !== 'undefined' ? map : null);

    if (!elMapa) {
        console.error("Error: No se encontró el mapa de Leaflet.");
        return;
    }

    // Agrega la capa al mapa si no existe
    if (!elMapa.hasLayer(capaSismos)) {
        capaSismos.addTo(elMapa);
    }

    // Limpia los sismos anteriores
    capaSismos.clearLayers();

    // Usa la variable de Django o una URL por defecto de la USGS
    const urlSismos = (typeof URL_API_SISMOS !== 'undefined') 
        ? URL_API_SISMOS 
        : "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson";

    fetch(urlSismos)
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                pointToLayer: function (feature, latlng) {
                    const magnitud = feature.properties.mag || 1;
                    let colorCirculo = '#2ecc71'; // Verde para < 3

                    if (magnitud >= 3 && magnitud < 5) colorCirculo = '#f39c12'; // Naranja
                    if (magnitud >= 5) colorCirculo = '#dc2626'; // Rojo para >= 5

                    return L.circleMarker(latlng, {
                        radius: Math.max(magnitud * 2.5, 4),
                        fillColor: colorCirculo,
                        color: '#000000',
                        weight: 0.8,
                        fillOpacity: 0.75
                    });
                },
                onEachFeature: function (feature, layer) {
                    const props = feature.properties;
                    const fecha = new Date(props.time).toLocaleString('es-ES');
                    const profundidad = feature.geometry.coordinates[2];

                    layer.bindPopup(`
                        <div style="font-family: sans-serif; font-size: 13px;">
                            <h3 style="margin: 0 0 5px 0; color: #1e293b;">🌋 Magnitud ${props.mag}</h3>
                            <b>Lugar:</b> ${props.place}<br>
                            <b>Fecha / Hora:</b> ${fecha}<br>
                            <b>Profundidad:</b> ${profundidad} km<br>
                            <a href="${props.url}" target="_blank" style="color: #2563eb; display: inline-block; margin-top: 5px;">Ver en USGS</a>
                        </div>
                    `);
                }
            }).addTo(capaSismos);
        })
        .catch(error => {
            console.error('Error al cargar sismos:', error);
            alert('No se pudieron obtener los datos de sismos en este momento.');
        });
}