class TimeLog:
    def __init__(self):
        self.t = 0

# questo oggetto serve per poter essere passato tramite reference alle funzioni (altrimenti un semplice valore sarebbe
# passato per copia) e non posso usare i return dato che alcune funzioni le usano
