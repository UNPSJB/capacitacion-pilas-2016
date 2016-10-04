import pilasengine
pilas = pilasengine.iniciar()


class Escena_Menu(pilasengine.escenas.Escena):

    "Es la escena que muestra el menu"
    # El texto anterior sera interpretado por Phyton para armar la
    # documentacion de la clase

    # Iniciamos el creador de la clase, esta funcion siempre debe estar
    # presente
    def iniciar(self):
        # Carga el fondo en una subruta
        pilas.fondos.Fondo("data/Menu.png")
        self.Crear_Menu_Principal()

    def Crear_Menu_Principal(self):
        pilas.actores.Menu([
            ("Comenzar juego", self.comenzar_a_juegar),
            ("Ver ayuda", self.ver_ayuda_del_juego),
            ("Salir", self.salir_del_juego)
        ])

    def comenzar_a_juegar(self):
        print "Inicia el juego"

    def ver_ayuda_del_juego(self):
        print "Ayuda"

    def salir_del_juego(self):
        print "salir"

pilas.escenas.vincular(Escena_Menu)
pilas.escenas.Escena_Menu()

pilas.ejecutar()
