import re


class BuscaEndereco:
    def __init__(self, cep):
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('O cep informado é inválido')

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
