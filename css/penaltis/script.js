/*=========================================
        PENALTY CHAMPIONS 2026
=========================================*/

const equipos = {

    colombia:{

        nombre:"🇨🇴 Colombia",

        color:"#FFD400",

        jugadores:[

            {nombre:"James Rodríguez",numero:10,posicion:"Volante",potencia:90,precision:94},

            {nombre:"Luis Díaz",numero:7,posicion:"Delantero",potencia:92,precision:88},

            {nombre:"Rafael Santos Borré",numero:19,posicion:"Delantero",potencia:85,precision:84},

            {nombre:"Jhon Arias",numero:11,posicion:"Extremo",potencia:83,precision:86},

            {nombre:"Yerry Mina",numero:13,posicion:"Defensa",potencia:80,precision:72}

        ]

    },

    argentina:{

        nombre:"🇦🇷 Argentina",

        color:"#6EC6FF",

        jugadores:[

            {nombre:"Lionel Messi",numero:10,posicion:"Delantero",potencia:97,precision:99},

            {nombre:"Julián Álvarez",numero:9,posicion:"Delantero",potencia:91,precision:91},

            {nombre:"Lautaro Martínez",numero:22,posicion:"Delantero",potencia:93,precision:90},

            {nombre:"Enzo Fernández",numero:8,posicion:"Volante",potencia:86,precision:88},

            {nombre:"Mac Allister",numero:20,posicion:"Volante",potencia:85,precision:87}

        ]

    },

    brasil:{

        nombre:"🇧🇷 Brasil",

        color:"#28B463",

        jugadores:[

            {nombre:"Vinicius Jr",numero:7,posicion:"Extremo",potencia:95,precision:90},

            {nombre:"Rodrygo",numero:10,posicion:"Delantero",potencia:92,precision:90},

            {nombre:"Raphinha",numero:11,posicion:"Extremo",potencia:90,precision:87},

            {nombre:"Bruno Guimarães",numero:8,posicion:"Volante",potencia:85,precision:84},

            {nombre:"Marquinhos",numero:4,posicion:"Defensa",potencia:81,precision:78}

        ]

    },

    francia:{

        nombre:"🇫🇷 Francia",

        color:"#0047AB",

        jugadores:[

            {nombre:"Mbappé",numero:10,posicion:"Delantero",potencia:98,precision:95},

            {nombre:"Griezmann",numero:7,posicion:"Delantero",potencia:90,precision:90},

            {nombre:"Dembélé",numero:11,posicion:"Extremo",potencia:91,precision:86},

            {nombre:"Tchouaméni",numero:8,posicion:"Volante",potencia:85,precision:82},

            {nombre:"Koundé",numero:5,posicion:"Defensa",potencia:80,precision:76}

        ]

    }

};

/*=========================================
VARIABLES
=========================================*/

const selectEquipo=document.getElementById("equipo");

const selectJugador=document.getElementById("jugador");

const nombreEquipo=document.getElementById("nombreEquipo");

const nombreJugador=document.getElementById("nombreJugador");

const tipoJugador=document.getElementById("tipoJugador");

const numeroJugador=document.getElementById("numeroJugador");

const potencia=document.getElementById("potencia");

const precision=document.getElementById("precision");

const lista=document.getElementById("listaJugadores");

const jugadorCancha=document.getElementById("jugadorCancha");

/*=========================================
CARGAR EQUIPO
=========================================*/

function cargarEquipo(){

    let equipo=equipos[selectEquipo.value];

    nombreEquipo.textContent=equipo.nombre;

    jugadorCancha.style.color=equipo.color;

    llenarSelect(equipo);

    llenarBanca(equipo);

    mostrarJugador(equipo.jugadores[0]);

}

/*=========================================
SELECT
=========================================*/

function llenarSelect(equipo){

    selectJugador.innerHTML="";

    equipo.jugadores.forEach((jugador,index)=>{

        let opcion=document.createElement("option");

        opcion.value=index;

        opcion.textContent=jugador.nombre;

        selectJugador.appendChild(opcion);

    });

}

/*=========================================
BANCA
=========================================*/

function llenarBanca(equipo){

    lista.innerHTML="";

    equipo.jugadores.forEach((jugador)=>{

        let div=document.createElement("div");

        div.textContent=jugador.nombre;

        lista.appendChild(div);

    });

}

/*=========================================
MOSTRAR JUGADOR
=========================================*/

function mostrarJugador(jugador){

    nombreJugador.textContent=jugador.nombre;

    tipoJugador.textContent=jugador.posicion;

    numeroJugador.textContent="Número "+jugador.numero;

    potencia.style.width=jugador.potencia+"%";

    precision.style.width=jugador.precision+"%";

}

/*=========================================
CAMBIAR EQUIPO
=========================================*/

selectEquipo.addEventListener("change",()=>{

    cargarEquipo();

});

/*=========================================
CAMBIAR JUGADOR
=========================================*/

selectJugador.addEventListener("change",()=>{

    let equipo=equipos[selectEquipo.value];

    let jugador=equipo.jugadores[selectJugador.value];

    mostrarJugador(jugador);

});

/*=========================================
INICIAR
=========================================*/

cargarEquipo();

/*=========================================
VARIABLES DEL JUEGO
=========================================*/

const botonesDireccion = document.querySelectorAll(".grid-direccion button");

const comentarios = document.getElementById("comentarios");

const pelota = document.getElementById("pelota");

const portero = document.getElementById("portero");

const marcadorGoles = document.getElementById("goles");

const marcadorAtajadas = document.getElementById("atajadas");

const pantallaFinal = document.getElementById("pantallaFinal");

const campeon = document.getElementById("campeon");

const reiniciar = document.getElementById("reiniciar");

let goles = 0;

let atajadas = 0;

let turno = 0;

/*=========================================
NARRADOR
=========================================*/

const frasesGol = [

"¡¡GOOOOOOOOOOOL!!",

"Disparo imposible para el portero.",

"El balón terminó en el fondo de la red.",

"Gran definición del cobrador."

];

const frasesAtajada = [

"¡¡ATAJADÓN!!",

"El portero adivinó la dirección.",

"Gran reacción del guardameta.",

"El disparo fue detenido."

];

/*=========================================
ESCRIBIR NARRACIÓN
=========================================*/

function narrar(texto){

    comentarios.innerHTML += "<p>"+texto+"</p>";

    comentarios.scrollTop = comentarios.scrollHeight;

}

/*=========================================
PORTERO
=========================================*/

function moverPortero(direccion){

    portero.style.transform="translateX(-50%)";

    if(direccion=="izquierda"){

        portero.style.transform="translateX(-180px)";

    }

    if(direccion=="derecha"){

        portero.style.transform="translateX(120px)";

    }

}

/*=========================================
PELOTA
=========================================*/

function moverPelota(direccion){

    pelota.style.bottom="470px";

    pelota.style.left="50%";

    if(direccion=="izquierda"){

        pelota.style.left="35%";

    }

    if(direccion=="derecha"){

        pelota.style.left="65%";

    }

}

/*=========================================
SIGUIENTE JUGADOR
=========================================*/

function siguienteJugador(){

    let equipo=equipos[selectEquipo.value];

    turno++;

    if(turno>=equipo.jugadores.length){

        finalizarJuego();

        return;

    }

    selectJugador.value=turno;

    mostrarJugador(equipo.jugadores[turno]);

}

/*=========================================
FINAL
=========================================*/

function finalizarJuego(){

    pantallaFinal.style.display="flex";

    campeon.textContent=selectEquipo.options[
        selectEquipo.selectedIndex
    ].text;

}

/*=========================================
REINICIAR
=========================================*/

reiniciar.addEventListener("click",()=>{

    goles=0;

    atajadas=0;

    turno=0;

    marcadorGoles.textContent="0";

    marcadorAtajadas.textContent="0";

    pantallaFinal.style.display="none";

    cargarEquipo();

    comentarios.innerHTML="<p>Comienza una nueva tanda.</p>";

});

/*=========================================
COBRAR PENAL
=========================================*/

botonesDireccion.forEach((boton)=>{

    boton.addEventListener("click",()=>{

        let direccionJugador=boton.dataset.dir;

        narrar("⚽ "+nombreJugador.textContent+" toma carrera...");

        let opciones=[

            "izquierda",

            "centro",

            "derecha"

        ];

        let direccionPortero=

        opciones[Math.floor(Math.random()*3)];

        moverPelota(direccionJugador);

        moverPortero(direccionPortero);

        setTimeout(()=>{

            if(

                direccionJugador.includes(direccionPortero)

            ){

                atajadas++;

                marcadorAtajadas.textContent=atajadas;

                narrar(

                frasesAtajada[

                Math.floor(Math.random()*frasesAtajada.length)

                ]

                );

            }

            else{

                goles++;

                marcadorGoles.textContent=goles;

                narrar(

                frasesGol[

                Math.floor(Math.random()*frasesGol.length)

                ]

                );

            }

            pelota.style.left="50%";

            pelota.style.bottom="150px";

            portero.style.transform="translateX(-50%)";

            siguienteJugador();

        },1000);

    });

});