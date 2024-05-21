# main.py

from bus_de_eventos import BusDeEventos
from manejadores import manejador_de_evento_a, manejador_de_evento_b

# Crear una instancia del Bus de Eventos
bus = BusDeEventos()

# Suscribir manejadores a eventos
bus.suscribir('evento_a', manejador_de_evento_a)
bus.suscribir('evento_b', manejador_de_evento_b)

# Publicar eventos
bus.publicar('evento_a', {'mensaje': 'Hola desde Evento A'})
bus.publicar('evento_b', {'mensaje': 'Hola desde Evento B'})

