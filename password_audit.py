senha = input("Digite uma senha: ")

tamanho = len(senha)

especiais = "!@#$%&*"

tem_numero = any(caractere.isdigit() for caractere in senha)

tem_maiuscula = any(caractere.isupper() for caractere in senha)

tem_minuscula = any(caractere.islower() for caractere in senha)

tem_especial = any(caractere in especiais for caractere in senha)

senha_valida= True

pontuacao = 0

if tamanho < 8:
    print("A senha precisa ter pelo menos 8 caracteres.")
    senha_valida = false

else:
        pontuacao += 1

if not tem_numero:
    print("A senha precisa de pelo menos um número")
    senha_valida = false

else:
        pontuacao += 1

if not tem_maiuscula:
    print("A senha precisa de pelo menos uma letra maiúscula")
    senha_valida = false

else: 
        pontuacao += 1

if not tem_minuscula:
    print("A senha precisa ter ao menos uma letra minúscula")
    senha_valida = false

else:
        pontuacao += 1

if not tem_especial:
    print("A senha precisa ter ao menos um especial")
    senha_valida = false

else: 
    pontuacao += 1


if senha_valida:
    print("Senha aprovada!")

print("pontuação", pontuacao)

if pontuacao == 5:
    print("Força da senha: FORTE")
elif pontuacao == 3:
    print("Força da senha: MÉDIA")
else:
    print("Força da senha: FRACA")

