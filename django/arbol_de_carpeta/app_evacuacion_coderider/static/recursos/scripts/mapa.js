var map = null;
var miMarcador = null;
var marcadorDestino = null;
var marcadorOrigen = null; // Marcador para el punto de origen manual
var lineaRuta = null;
var capaSismos = null;
var miPosicion = null;

var latBase = 2.4419;
var lngBase = -76.6063;

// Variables para controlar la lógica de 2 clics (Origen -> Destino)
var estadoClic = "origen"; 
var origenSeleccionado = null; 

document.addEventListener('DOMContentLoaded', function() {
    var mapContainer = document.getElementById('mapa');
    if (!mapContainer) return;

    // 1. Inicializar mapa
    map = L.map('mapa').setView([latBase, lngBase], 14);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors, Humanitarian OpenStreetMap Team'
    }).addTo(map);

    // Inicializar la capa para los sismos
    capaSismos = L.layerGroup().addTo(map);

    // Ajustar renderizado visual
    setTimeout(function() {
        map.invalidateSize();
    }, 400);

    // 2. LÓGICA DE DOS CLICS (Primer clic: Origen, Segundo clic: Destino)
    map.on('click', function(e) {
        if (estadoClic === "origen") {
            // Primer clic: Limpia rutas previas y guarda origen
            limpiarRuta(); 
            origenSeleccionado = e.latlng;
            
            marcadorOrigen = L.marker(origenSeleccionado).addTo(map)
                .bindPopup("<b>📍 Punto de Partida</b><br>Haz clic en otro punto para marcar tu destino.").openPopup();
            
            estadoClic = "destino";
        } else {
            // Segundo clic: Trazar la ruta hacia el destino
            trazarRutaADestino(e.latlng);
            estadoClic = "origen"; // Reinicia el ciclo
        }
    });

    // 3. Cargar puntos de encuentro desde JSON
    if (typeof URL_JSON !== 'undefined' && URL_JSON) {
        fetch(URL_JSON)
            .then(res => res.json())
            .then(puntos => {
                puntos.forEach(p => {
                    if (p.lat && p.lng) {
                        L.marker([p.lat, p.lng]).addTo(map)
                            .bindPopup(`
                                <b>${p.nombre || 'Punto de Encuentro'}</b><br>
                                ${p.descripcion || ''}<br><br>
                                <button onclick="trazarRutaADestino(L.latLng(${p.lat}, ${p.lng}))" style="background:#16a34a; color:#fff; border:none; padding:5px 10px; border-radius:4px; cursor:pointer;">
                                    🚗 Trazar Ruta Aquí
                                </button>
                            `);
                    }
                });
            })
            .catch(err => console.log("Aviso JSON:", err));
    }

    // 4. Cargar GeoJSON de ruta
    if (typeof URL_GEO !== 'undefined' && URL_GEO) {
        fetch(URL_GEO)
            .then(res => res.json())
            .then(geoData => {
                L.geoJSON(geoData, {
                    style: { color: '#dc2626', weight: 4, opacity: 0.8 }
                }).addTo(map);
            })
            .catch(err => console.log("Aviso GeoJSON:", err));
    }
});

// ==========================================
// FUNCIONES DE LOS BOTONES Y RUTAS
// ==========================================

// 📍 1. Mi Ubicación (GPS)
window.miUbicacionGPS = function() {
    if (!navigator.geolocation) {
        alert("Tu navegador no soporta geolocalización.");
        return;
    }

    navigator.geolocation.getCurrentPosition(
        function(pos) {
            var lat = pos.coords.latitude;
            var lng = pos.coords.longitude;
            miPosicion = L.latLng(lat, lng);

            if (miMarcador) {
                miMarcador.setLatLng(miPosicion);
            } else {
                miMarcador = L.marker(miPosicion).addTo(map)
                    .bindPopup('<b>📍 Mi Ubicación Actual</b>');
            }

            map.setView(miPosicion, 16);
            miMarcador.openPopup();
        },
        function(err) {
            alert("Para ver tu ubicación debes permitir el acceso al GPS en el navegador. Error: " + err.message);
        },
        { enableHighAccuracy: true }
    );
};

// 🎯 2. Centrar Mapa
window.centrarMapa = function() {
    if (map) {
        map.setView([latBase, lngBase], 14);
    }
};

// 🌋 3. Ver Sismos Recientes
window.verSismos = function() {
    if (!map) return;

    // Si la capa aún no ha sido agregada al mapa, la creamos
    if (!capaSismos) {
        capaSismos = L.layerGroup().addTo(map);
    }

    capaSismos.clearLayers();

    var url = typeof URL_API_SISMOS !== 'undefined' ? URL_API_SISMOS : "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson";

    fetch(url)
        .then(res => res.json())
        .then(data => {
            var contador = 0;
            data.features.forEach(f => {
                var c = f.geometry.coordinates;
                var mag = f.properties.mag;
                var color = mag >= 5.0 ? '#dc2626' : (mag >= 3.5 ? '#ea580c' : '#eab308');

                L.circleMarker([c[1], c[0]], {
                    radius: Math.max(mag * 3, 4),
                    color: color,
                    fillColor: color,
                    fillOpacity: 0.7
                }).bindPopup(`<b>⚠️ Sismo Magnitud ${mag}</b><br>${f.properties.place}`).addTo(capaSismos);

                contador++;
            });
            alert("Se mostraron " + contador + " sismos recientes en el mapa.");
        })
        .catch(err => alert("Error al cargar sismos: " + err));
};

// ❌ 4. Limpiar Ruta
window.limpiarRuta = function() {
    if (lineaRuta && map) map.removeLayer(lineaRuta);
    if (marcadorDestino && map) map.removeLayer(marcadorDestino);
    if (marcadorOrigen && map) map.removeLayer(marcadorOrigen);
    
    lineaRuta = null;
    marcadorDestino = null;
    marcadorOrigen = null;
    origenSeleccionado = null;
    estadoClic = "origen"; // Reinicia el flujo al primer clic
};

// 🚗 5. Trazar Ruta al hacer Clic en el Mapa
window.trazarRutaADestino = function(destinoLatLng) {
    if (lineaRuta && map) map.removeLayer(lineaRuta);
    if (marcadorDestino && map) map.removeLayer(marcadorDestino);

    // Prioridad de Origen: 1. Clic manual -> 2. Ubicación GPS -> 3. Popayán base
    var origen = origenSeleccionado || miPosicion || L.latLng(latBase, lngBase);

    marcadorDestino = L.marker(destinoLatLng).addTo(map)
        .bindPopup("<b>🏁 Calculando ruta...</b>").openPopup();

    var urlOSRM = `https://router.project-osrm.org/route/v1/driving/${origen.lng},${origen.lat};${destinoLatLng.lng},${destinoLatLng.lat}?overview=full&geometries=geojson`;

    fetch(urlOSRM)
        .then(res => res.json())
        .then(data => {
            if (data.routes && data.routes.length > 0) {
                var route = data.routes[0];
                var coords = route.geometry.coordinates.map(c => [c[1], c[0]]);

                lineaRuta = L.polyline(coords, { color: '#2563eb', weight: 6, opacity: 0.85 }).addTo(map);
                map.fitBounds(lineaRuta.getBounds(), { padding: [30, 30] });

                var km = (route.distance / 1000).toFixed(2);
                var min = Math.round(route.duration / 60);

                marcadorDestino.setPopupContent(`<b>🏁 Destino Seleccionado</b><br>Distancia: ${km} km<br>Tiempo est.: ${min} min`).openPopup();
            } else {
                alert("No se encontró una ruta vial hacia este punto.");
            }
        })
        .catch(err => console.error("Error calculando ruta:", err));
};