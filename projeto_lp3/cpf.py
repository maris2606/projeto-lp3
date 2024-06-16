from validate_docbr import CPF
cpf = CPF()

# gerar com mascara
print(cpf.generate(True))
print(cpf.generate(False))

cpf_valido = cpf.generate()

# meu cpf
print(cpf.validate(["45856595622"]))
print(cpf.validate([cpf_valido]))