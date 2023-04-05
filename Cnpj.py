from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!!")

    def valida_cnpj(self, documento):
        if len(documento) == 14:
            validator = CNPJ()
            return validator.validate(documento)
        else:
            return False

    def masked_cnpj(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):
        return self.masked_cnpj()
