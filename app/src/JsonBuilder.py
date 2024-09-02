import json

from . import DataValidator
from . import MarkeyAPI
from . import Paciente


# consulta = MarkeyAPI().getResponse(dni="1")
# validator = DataValidator(consulta)
#
# lista = []
# for paciente in validator.getPacientes():
#     p = Paciente(nombre=validator.getFirstname(paciente), apellido=validator.getLastname(paciente),
#                  fechaNacimiento=validator.getBirthDate(paciente),
#                  email=validator.getEmail(paciente),
#                  phone=validator.getPhone(paciente),
#                  dni=validator.getDni(paciente),
#                  historiaClinica=validator.getHistClinica(paciente),
#                  tipoDocumento=validator.getTipoDocumento(paciente),
#                  cobertura=validator.getCobertura(paciente),
#                  planContratado=validator.getPlanContratado(paciente),
#                  codigoAfiliado=validator.getCodAfiliado(paciente))
#     print(json.dumps(p.jsonFormat()))
#
#
