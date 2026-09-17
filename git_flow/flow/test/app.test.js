import {saludar, despedir, estadosistema, sumar, healthcheck} from "../src/app.js"

function ejecutarpruebas() {
let pasado =0;
let fallidas = 0;

const r1 = saludar("hamilton")
if (r1.includes("hamilton")){
console.log ("test 1 paso: funcion saludar es correcta")
pasado++;
} else {
console.log("test 1 fallido:", r1 );
fallidas++;
}

const actualestado = estadosistema();
if (actualestado.estado === "activo"){
console.log ("test 2: estadosistema()");
pasado++;
}else{
// Cambié 'estado' por 'actualestado.estado' para que no dé error
console.log("test 2: fallido", actualestado.estado, "en hamilton");
fallidas++;
}


const resultadoSuma = sumar(5, 10);
if (resultadoSuma === 15) {
    console.log(" Test 3 pasó: sumar(5, 10) es 15");
    pasado++;
} else {
    console.log(" Test 3 fallido: se esperaba 15 pero dio " + resultadoSuma);
    fallidas++;
}
const health = healthcheck();
if (health.status === 'ok'){
    console.log(' test healthcheck pasado');
    pasado++;
}else {
    console.log(' test healthcheck fallido", health');
    fallidas++;
}

console.log ("\nresultados: " + pasado +"pasado, ", + fallidas + "fallidas");

if(fallidas>0) process.exit(1);

}

ejecutarpruebas();