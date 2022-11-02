class ManejoArchivos:

    def __init__(self,nombre):
        self.nombre=nombre

    def __enter__(self):
        print('Obrenemos el recurso'.center(50,'-'))
        self.nombre=open(self.nombre,'r',encoding='utf8')

        return self.nombre

    def __exit__(self, tipo_exceptio,valor_exception,traza_error):
        print('cerramos recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()
