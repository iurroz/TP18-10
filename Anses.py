from main import Usuario

database = [(13,120, "Marcos"), (12,110, "teodoro"), (11,100, "Iñaki" )]

class Info (Usuario):


    def contacto (self):

        if database[self.i][0] == Usuario.Cuil and database[self.i][1] == Usuario.Celu:
            return database [self.i][2]
        else:
            return Info.contacto (self.i-1)

print(Info(Usuario.Cuil, Usuario.Celu, len(database)))









