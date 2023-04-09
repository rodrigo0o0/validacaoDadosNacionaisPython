# from TelefonesBr import TelephonesBr
import re


telefone = ' +55    (48)99663- 6643'
telefone = (re.sub(" ", "", telefone))

regex = r"\d{0,2}\(?\d{2}\)?\d{4,5}\-?\d{4}$"
resultado = re.search(regex, telefone)
if resultado != None:
    print("Número váido")
else:
    raise ValueError("Número inválido")

# telefone = TelephonesBr('489966336643')
# print(telefone)


'''from cpf_cnpj import Document


cpf_1 = '07642631960'
cnpj_1 = '54492221750586'

cpf = Document.create_document(cpf_1)
cnpj = Document.create_document(cnpj_1)


print(cnpj)
print(cpf)
'''
