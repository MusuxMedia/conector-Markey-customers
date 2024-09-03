class DataValidator:
    def __init__(self, json_dict):
        self.data = json_dict["data"]

    def isValid(self):
        return len(self.data) > 0

    def getPacientes(self):
        try:
            return self.data["Pacientes"]
        except KeyError:
            return ""

    def getCoberturas(self, paciente):
        try:
            return paciente["Coberturas"]
        except KeyError:
            return ""

    def isValidCoberturas(self, paciente):
        return len(self.getCoberturas(paciente)) > 0

    def getFirstname(self, paciente):
        try:
            return paciente["persNombre"]
        except KeyError:
            return ""

    def getLastname(self, paciente):
        try:
            return paciente["persApellido"]
        except KeyError:
            return ""

    def getDni(self, paciente):
        try:
            return paciente["persNroDocumento"]
        except KeyError:
            return ""

    def getEmail(self, paciente):
        try:
            return paciente["persMail"]
        except KeyError:
            return ""

    def getPhone(self, paciente):
        try:
            return paciente["persTelefonoCelular"]
        except KeyError:
            return ""

    def getBirthDate(self, paciente):
        try:
            return paciente["persFechaNacimiento"]
        except KeyError:
            return ""

    def getHistClinica(self, paciente):
        try:
            return paciente["paciHistoriaClinica"]
        except KeyError:
            return ""

    def getCobertura(self, paciente):
        if (self.isValidCoberturas(paciente)):
            return [cobertura["cobeDescripcion"] for cobertura in self.getCoberturas(paciente)]
        else:
            return ""

    def getTipoDocumento(self, paciente):
        try:
            return paciente["tdocDescripcion"]
        except KeyError:
            return ""

    def getPlanContratado(self, paciente):
        if self.isValidCoberturas(paciente):
            return [cobertura["planDescripcion"] for cobertura in self.getCoberturas(paciente)]
        else:
            return ""

    def getCodAfiliado(self, paciente):
        try:
            if self.isValidCoberturas(paciente):
                return [cobertura["pacoAfiliado"] for cobertura in self.getCoberturas(paciente)]
            else:
                return ""
        except KeyError:
            return ""
