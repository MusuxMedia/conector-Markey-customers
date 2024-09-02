import json

from . import DataValidator


class Paciente(dict):
    def __init__(self, nombre, apellido, fechaNacimiento, email, phone, dni, historiaClinica, tipoDocumento, cobertura,
                 planContratado, codigoAfiliado):
        dict.__init__(self)
        self.nombre = nombre
        self.apellido = apellido
        self.fechaNacimiento = fechaNacimiento
        self.email = email
        self.phone = phone
        self.dni = dni
        self.historiaClinica = historiaClinica
        self.tipoDocumento = tipoDocumento
        self.cobertura = cobertura
        self.planContratado = planContratado
        self.codigoAfiliado = codigoAfiliado

    def __repr__(self):
        return self.toJson()

    def toJson(self):
        return {
            "firstName": self.nombre,
            "lastName": self.apellido,
            "dni": self.dni,
            "email": self.email,
            "selectionName": self.fechaNacimiento,
            "phone": self.phone,
            "customerType" : 829, #harcodeado, hay que pasarlo a variable
            "extraFields": [
                {
                    "showable": [
                        {
                            "in": "workstation",
                            "format": "both"
                        }
                    ],
                    "NHC": self.historiaClinica
                },
                {
                    "showable": [
                        {
                            "in": "workstation",
                            "format": "both"
                        }
                    ],
                    "tdocDescripcion": self.tipoDocumento
                },
                {
                    "showable": [
                        {
                            "in": "workstation",
                            "format": "both"
                        }
                    ],
                    "cobeDescripcion": self.cobertura
                },
                {
                    "showable": [
                        {
                            "in": "workstation",
                            "format": "both"
                        }
                    ],
                    "planDescripcion": self.planContratado
                },
                {
                    "showable": [
                        {
                            "in": "workstation",
                            "format": "both"
                        }
                    ],
                    "pacoAfiliado": self.codigoAfiliado
                }
            ]
        }


# print(Paciente("<NAME>", "<NAME>", "12/4/5678", "12/4/5678", "12/4, 5678", "12/4, 5678", "12/4, 5678", "12/4", "OSDE",
#                "12/4/5678", "12"))

