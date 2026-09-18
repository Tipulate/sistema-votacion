# SISTEMA DE VOTACION

## `registrar_voto()`

Pide un identificador (cédula/usuario), lo hashea con SHA-256, revisa que no haya votado antes, pide la opción (1 o 2), la valida, y si todo está bien guarda el voto en `usuarios` y suma en `votos`.

## `ver_resultados()`

Cuenta los votos totales, calcula cuántos y qué porcentaje le tocó a cada equipo, e imprime el resumen. Si no hay votos todavía, avisa y corta ahí.

## `reiniciar_votacion()`

El nombre engaña un poco: no reinicia nada, exporta `usuarios` y `votos` a dos CSV (`usuarios.csv` y `votos.csv`).

## `menu()`

Imprime las opciones del menú en pantalla.

## Loop principal (`while True`)

Muestra el menú, lee la opción elegida y llama a la función correspondiente. Con "4" rompe el loop y termina el programa.
