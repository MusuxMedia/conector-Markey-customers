from . import MarkeyAPI
from . import DataValidator
from . import Paciente
from .config import Settings


class ProcessOrganizer:
    def __init__(self, dni: str, credenciales):
        self.dni = dni
        self.credenciales = credenciales

    def validate_data(self):
        markey_response = MarkeyAPI(self.credenciales).getResponse(self.dni)
        validator: DataValidator = DataValidator(markey_response)
        if validator.isValid():
            return self.build_paciente(validator)
        else:
            return self.build_dummy()

    def build_paciente(self, validator: DataValidator):
        lista = []
        for paciente in validator.getPacientes():
            p = Paciente(nombre=validator.getFirstname(paciente), apellido=validator.getLastname(paciente),
                         fechaNacimiento=validator.getBirthDate(paciente),
                         email=validator.getEmail(paciente),
                         phone=validator.getPhone(paciente),
                         dni=validator.getDni(paciente),
                         historiaClinica=validator.getHistClinica(paciente),
                         tipoDocumento=validator.getTipoDocumento(paciente),
                         cobertura=validator.getCobertura(paciente),
                         planContratado=validator.getPlanContratado(paciente),
                         codigoAfiliado=validator.getCodAfiliado(paciente),
                         customerType=self.credenciales.CUSTOMERTYPE)
            lista.append(p.toJson())
        return lista

    def build_dummy(self):
        return [
            {
                "firstName": "N/P",
                "lastName": "N/P",
                "dni": self.dni,
                "customerType": {
                    "id": "799"
                },
                "extraFields":
                    {
                        "NHC": "N/A"
                    }
            }
        ]
