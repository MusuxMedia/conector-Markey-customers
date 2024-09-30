from ast import literal_eval
from fastapi import HTTPException

class DisplayParser:

    def parse(self, pantallas: str) -> list[int]:
        try:
            lista = literal_eval(pantallas)
            self.validate_list(lista)
            return lista
        except SyntaxError:
            raise HTTPException(status_code=401,
                                detail="Display incorrecto, recordar utilizar [] y separar los valores por coma")
        except ValueError:
            raise HTTPException(status_code=402, detail="Display incorrecto, el valor debe ser un array de numero/s")

    def validate_list(self, lista_pantallas):
        self.esta_vacia(lista_pantallas)
        self.contiene_enteros(lista_pantallas)

    def contiene_enteros(self, lista_pantallas):
        if not(all(isinstance(n, int) for n in lista_pantallas)):
            raise HTTPException(status_code=405, detail="El Display únicamente deben ser numero enteros")

    def esta_vacia(self, lista_pantallas):
        if len(lista_pantallas) == 0:
            raise HTTPException(status_code=403, detail="El Display no puede estar vacio")
