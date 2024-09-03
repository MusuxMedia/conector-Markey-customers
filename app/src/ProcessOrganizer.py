from . import MarkeyAPI
from . import DataValidator
from . import Paciente


class ProcessOrganizer:
    def __init__(self, dni: str, credenciales):
        self.dni = dni
        self.credenciales = credenciales

    # Consultar datos
    # Validar si es paciente
    # Enviar datos de los pacientes         # Sino enviar NHC con "No Cliente" y el customerType de no cliente
    def validate_data(self):
        validator: DataValidator = DataValidator(MarkeyAPI(self.credenciales).getResponse(self.dni))
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
        print(lista)
        return lista

    def build_dummy(self):
        print([
            {
                "customerType": self.credenciales.NO_CUSTOMERTYPE,
                "extraFields": [
                    {
                        "showable": [
                            {
                                "in": "workstation",
                                "format": "both"
                            }
                        ],
                        "NHC": "No Cliente"
                    },
                ]
            }
        ])
        return [
            {
                "customerType": 799,
                "extraFields": [
                    {
                        "showable": [
                            {
                                "in": "workstation",
                                "format": "both"
                            }
                        ],
                        "NHC": "No Cliente"
                    }
                ]
            }
        ]
