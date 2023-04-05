from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, document, doc_type):
        self.doc_type = doc_type
        if doc_type == 'cpf':
            if self.validate_cpf(document):
                self.cpf = document
            else:
                raise ValueError("Cpf inválido")
        elif doc_type == 'cnpj':
            if self.validate_cnpj(document):
                self.cnpj = document
            else:
                raise ValueError("CNPJ inválido")

    def validate_cpf(self, document):
        if len(document) == 11:
            validador_cpf = CPF()
            return validador_cpf.validate(document)

        else:
            return False

    def validate_cnpj(self, document):
        if len(document) == 14:
            validador_cnpj = CNPJ()
            return validador_cnpj.validate(document)

        else:
            return False

    def masked_cpf(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def masked_cnpj(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)

    def __str__(self):
        if self.doc_type == 'cpf':
            return self.masked_cpf()
        elif self.doc_type == 'cnpj':
            return self.masked_cnpj()
        else:
            raise ValueError("Não foi gerada nenhuma instância.")
