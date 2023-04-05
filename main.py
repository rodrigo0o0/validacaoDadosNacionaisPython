from cpf_cnpj import CpfCnpj


cpf_1 = '07642631960'
cnpj_1 = '54492221750586'

cpf = CpfCnpj(cpf_1, "cpf")
cnpj = CpfCnpj(cnpj_1, "cnpj")


print(cnpj)
print(cpf)
