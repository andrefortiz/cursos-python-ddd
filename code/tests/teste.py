import inspect

from utils.serializers.AnonType import AnonType


def my_function(**data):
    schoolname  = data['school']
    cityname = data['school']
    standard = data['school']
    studentname = data['school']

class Teste:
    id = None
    nome = None

    def select(self, list, action):

        if list is not None:
            return [action(m) for m in list]





test = Teste()
#teste.id = 1
#teste.nome = "Andre"
data = (test.id, test.nome)
#my_function(**{'id', 'nome', 'solicitante=numero' })

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name






dog = Dog(
    age=1,
    name="Rover"
)

teste = AnonType(
    age=dog.age,
    name=dog.name
)

dog1 = Dog(
    age=6,
    name="Isquilate"
)

dog3 = Dog(
    age=8,
    name="Teus Beiços"
)


lista = [dog, dog1, dog3]

print(test.select(lista, lambda x: AnonType(age=x.age, name=x.name)))
