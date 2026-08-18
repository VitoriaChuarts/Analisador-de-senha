senha = input("Crie uma senha:")
tamanho = len (senha)
print(tamanho)

tem_numero = any(caractere.isdigit()for caractere in senha)
print(tem_numero)

if tamanho >= 8 and tem_numero:
    print("A senha atende aos requisitos.")
else:
    print("A senha não atende aos requisitos.")
