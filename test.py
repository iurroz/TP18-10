database = [(13,120, "Marcos"), (12,110, "teodoro"), (11,100, "Iñaki" )]

Cuil=input("cuil")
Celu= input("celu")

class Info :

    def __init__(self, i):
        self.i=i


    def contacto (self):

        if database[self.i][0] == Cuil and database[self.i][1] == Celu:
            return database [self.i][2]
        else:
            return Info.contacto (self.i-1)

result = Info(len(database))

print(Info(result))
