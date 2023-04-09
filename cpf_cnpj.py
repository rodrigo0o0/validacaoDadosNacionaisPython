from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create_document(document):
        size_doc = len(document)
        if size_doc == 11:
            return DocCpf(document)
        elif size_doc == 14:
            return DocCnpj(document)
        else:
            raise ValueError("Valor inválido")


class DocCpf:
    def __init__(self, document):
        if self.validate_cpf(document):
            self.cpf = document
        else:
            raise ValueError("Cpf inválido")

    def validate_cpf(self, document):
        if len(document) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(document)

        else:
            return False

    def masked_cpf(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return self.masked_cpf()


class DocCnpj:
    def __init__(self, document):
        if self.validate_cnpj(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ inválido")

    def validate_cnpj(self, document):
        if len(document) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(document)

        else:
            return False

    def masked_cnpj(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):

        return self.masked_cnpj()
