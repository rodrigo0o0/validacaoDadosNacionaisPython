import re


class TelephonesBr:
    def __init__(self, telefone):
        self.telefone = self.valida_telefone(telefone)

    def valida_telefone(telefone):
        regex = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        return (re.findall(regex, telefone))
