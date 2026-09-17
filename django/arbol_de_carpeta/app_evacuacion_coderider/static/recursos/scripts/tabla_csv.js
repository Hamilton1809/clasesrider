document.addEventListener('DOMContentLoaded', function() {
    var contenedor = document.getElementById('contenedor-tabla-csv');
    if (!contenedor || typeof URL_CSV === 'undefined' || !URL_CSV) return;

    fetch(URL_CSV)
        .then(res => {
            if (!res.ok) throw new Error("No se encontró el archivo CSV en " + URL_CSV);
            return res.text();
        })
        .then(csvText => {
            var lineas = csvText.split(/\r?\n/).filter(l => l.trim() !== '');
            if (lineas.length === 0) return;

            var html = '<div style="overflow-x:auto;"><table style="width:100%; border-collapse:collapse; background:#fff; border-radius:6px; overflow:hidden; border:1px solid #e2e8f0; margin-top:10px;">';

            lineas.forEach((linea, index) => {
                var cols = linea.split(',');
                html += '<tr style="border-bottom:1px solid #e2e8f0;">';
                
                cols.forEach(col => {
                    var textoLimpio = col.replace(/^"|"$/g, '').trim();
                    if (index === 0) {
                        html += `<th style="padding:10px; background:#f1f5f9; text-align:left; font-size:14px; color:#334155; font-weight:bold;">${textoLimpio}</th>`;
                    } else {
                        html += `<td style="padding:10px; font-size:13px; color:#475569;">${textoLimpio}</td>`;
                    }
                });

                html += '</tr>';
            });

            html += '</table></div>';
            contenedor.innerHTML = html;
        })
        .catch(err => {
            console.warn("Aviso CSV:", err.message);
            contenedor.innerHTML = `<p style="color:#dc2626; font-size:13px;">No se pudo cargar la vista previa de los datos (${err.message}).</p>`;
        });
});