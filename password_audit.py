print("================================")
print("       ANALISADOR DE SENHA")
print("================================")

senha = input("Digite uma senha: ")

tamanho = len(senha)

especiais = "!@#$%&*"

tem_numero = any(caractere.isdigit() for caractere in senha)

tem_maiuscula = any(caractere.isupper() for caractere in senha)

tem_minuscula = any(caractere.islower() for caractere in senha)

tem_especial = any(caractere in especiais for caractere in senha)

senha_valida= True

pontuacao = 0

if tamanho >= 8:
    print("[✓] Pelo menos 8 caracteres")
else:
    print("[✗] Pelo menos 8 caracteres")
    senha_valida = False


if tem_numero:
    print("[✓] Possui número")
else:
    print("[✗] Possui número")
    senha_valida = False


if tem_maiuscula:
    print("[✓] Possui letra maiúscula")
else:
    print("[✗] Possui letra maiúscula")
    senha_valida = False

if tem_minuscula:
    print("[✓] Possui letra minúscula")
else:
    print("[✗] Possui letra minúscula")
    senha_valida = False

if tem_especial:
    print("[✓] Possui caractere especial")
else:
    print("[✗] Possui caractere especial")
    senha_valida = False


print("--------------------------------")
print("Pontuação:", pontuacao, "/5")

if pontuacao == 5:
    print("Força: FORTE")
elif pontuacao >= 3:
    print("Força: MÉDIA")
else:
    print("Força: FRACA")

if senha_valida:
    print("Status: SENHA APROVADA")
else:
    print("Status: SENHA NÃO APROVADA")

print("================================")

