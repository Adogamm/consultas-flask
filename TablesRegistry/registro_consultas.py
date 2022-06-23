
class RegistroConsulta:

    def registro(self, accion):
        try:
            fichero_auditorias = open("Files/relaciones de tablas.txt")
        except FileNotFoundError:
            fichero_auditorias = open("Files/relaciones de tablas.txt","w")
            fichero_auditorias.write(accion)
            fichero_auditorias.close()
        else:
            fichero_auditorias = open("Files/relaciones de tablas.txt","w")
            fichero_auditorias.write(accion)
            fichero_auditorias.close()
