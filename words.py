import random
# Palabras en minúsculas, sin tildes ni ñ, sin espacios.
# Se escriben separadas por espacios o saltos de línea.
# Si alguna se repite, sorted(set(...)) la deja una sola vez.
WORDS = sorted(set("""
casa perro gato libro mesa silla puerta ventana techo pared
cocina bosque jardin planta arbol flor hoja fruta manzana naranja
pera uva limon cereza melon sandia papaya mango banana coco
pollo carne pescado arroz frijol leche queso huevo pan sopa
ensalada helado dulce postre cafe jugo vino agua cuchara tenedor
cuchillo plato vaso olla sarten horno nevera estufa bicicleta carro
moto bus tren avion barco puerto aeropuerto estacion camino calle
avenida carretera puente ciudad pueblo pais region frontera montana valle
rio lago oceano playa arena costa isla selva desierto volcan
nube lluvia viento trueno rayo nieve granizo niebla verano invierno
primavera semana minuto segundo hora reloj calendario cuaderno lapiz borrador
regla tijera pegamento papel carpeta mochila maleta bolso cartera llave
candado espejo cepillo jabon toalla almohada cobija colchon sabana lampara
vela foco bombillo interruptor enchufe cable bateria cargador teclado pantalla
raton monitor impresora computador laptop tableta celular telefono aplicacion navegador
programa variable funcion bucle cadena entero lista diccionario tupla conjunto
modulo algoritmo compilador sintaxis error proyecto tarea examen parcial materia
profesor estudiante alumno maestro director universidad colegio escuela biblioteca laboratorio
medico enfermera doctor hospital farmacia abogado juez policia bombero soldado
agricultor pescador panadero carpintero pintor musica cancion guitarra piano violin
flauta trompeta tambor concierto orquesta cine pelicula teatro actor escena
novela poema cuento historia leyenda dragon unicornio sirena gigante fantasma
tigre leon oso lobo zorro conejo vaca caballo cerdo gallina
pato pavo oveja cabra delfin ballena tiburon pulpo medusa hormiga
abeja mariposa escarabajo grillo serpiente lagartija tortuga cocodrilo rana aguila
halcon paloma loro pinguino canguro koala cebra rinoceronte hipopotamo hiena
camello ardilla castor erizo topo cuerpo cabeza brazo pierna mano
dedo ojo oreja nariz boca cerebro hueso musculo sangre piel
pelo diente lengua rodilla tobillo amigo familia hermano hermana abuelo
madre padre tio primo sobrino vecino novio esposa hijo nieto
felicidad tristeza miedo calma sorpresa valor amor respeto honestidad paciencia
verdad mentira deseo recuerdo promesa secreto destino esperanza confianza libertad justicia igualdad
mapa tesoro viaje aventura misterio deporte pelota cancha equipo partido torneo
medalla trofeo ganador meta salto correr nadar saltar bailar cantar
escribir leer dibujar pintar hablar escuchar mirar pensar sentir recordar
comprar vender pagar cobrar ahorrar aprender practicar entrenar crear construir
ayudar buscar encontrar perder ganar empezar terminar cerrar abrir cambiar
mover subir bajar girar caer lavar planchar cocinar limpiar barrer
viajar llegar salir volver quedar grande fuerte tranquilo contento alegre
alto bajo ancho largo corto nuevo viejo joven fresco caliente
suave duro blando claro oscuro bonito feo sucio limpio sencillo
interesante divertido aburrido curioso generoso amable honesto valiente listo sabio
rojo azul verde amarillo negro blanco morado rosado gris celeste
dorado lunes martes jueves viernes domingo enero febrero marzo abril mayo
junio julio agosto septiembre octubre noviembre diciembre fiesta navidad pascua
carnaval festival sol luna estrella planeta cometa marte saturno venus galaxia
universo cristal diamante metal oro plata bronce hierro cobre piedra roca
madera vidrio tela lana seda camisa falda vestido chaqueta guante bufanda
zapato corbata anillo pulsera moneda billete dinero precio cuenta
""".split()))
def choose_word():
    """Devuelve una palabra de la lista, elegida al azar."""
    return random.choice(WORDS)