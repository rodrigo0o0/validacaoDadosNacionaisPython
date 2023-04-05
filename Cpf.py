from validate_docbr import CPF


class Cpf:

    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido")

    def valida_cpf(self, documento):
        if len(documento) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(documento)

        else:
            return False

    def masked_cpf(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return self.masked_cpf()
