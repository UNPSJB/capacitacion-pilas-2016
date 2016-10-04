# encoding: utf-8
"""
Ejemplo de la documentación.
"""

import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Selva()


def iniciar_juego():
    print "Tengo que iniciar el juego"


def salir_del_juego():
    print "Tengo que salir..."

pilas.actores.Menu(
    [
        ('iniciar juego', iniciar_juego),
        ('salir', salir_del_juego),
    ])

pilas.ejecutar()
