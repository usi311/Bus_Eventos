# bus_de_eventos.py

class BusDeEventos:
    def __init__(self):
        self.suscriptores = {}

    def suscribir(self, evento, manejador):
        if evento not in self.suscriptores:
            self.suscriptores[evento] = []
        self.suscriptores[evento].append(manejador)

    def publicar(self, evento, datos=None):
        if evento in self.suscriptores:
            for manejador in self.suscriptores[evento]:
                manejador(datos)

