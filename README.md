Analisador de Senha

Projeto de cibersegurança desenvolvido em Python para analisar a força de senhas. O sistema verifica tamanho, presença de letras maiúsculas/minúsculas, números e caracteres especiais, calcula a entropia estimada e classifica a senha como Fraca, Média ou Forte.

O objetivo é boas práticas de criação de senhas e conceitos básicos de segurança digital.

Funcionalidades:
✅ Verificação de tamanho mínimo configurável
✅ Checagem de letras maiúsculas, minúsculas, números e caracteres especiais
✅ Comparação com uma lista de senhas comuns/vazadas
✅ Cálculo de entropia (bits) com base no espaço de caracteres usado
✅ Classificação final: Senha Fraca, Senha Média, Senha Forte ou Senha Comum
✅ Leitura segura da senha no terminal (não exibida na tela, via getpass)
 Como funciona:

O script pontua a senha em 6 critérios:

Critério	Descrição
Tamanho OK	(Tem pelo menos o tamanho mínimo definido)
Tem Número	(Contém ao menos um dígito)
Tem Maiúscula	(Contém ao menos uma letra maiúscula)
Tem Minúscula	(Contém ao menos uma letra minúscula)
Tem Especial	(Contém ao menos um caractere especial)
Não é Comum	(Não está na lista de senhas mais usadas)

A partir da quantidade de critérios atendidos e da entropia estimada, a senha recebe uma classificação final de força.

Pré-requisitos
Python 3.10 ou superior (usa from __future__ import annotations)

Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python (getpass, math, re, dataclasses).

 Como usar

Clone o repositório:

bash
git clone https://github.com/VitoriaChuarts/Analisador-de-senha.git
cd Analisador-de-senha

Execute o script:

bash
python password_audit.py

Digite a senha quando solicitado (ela não será exibida no terminal por segurança).

📋 Exemplo de saída
Digite uma senha (não será exibida): 
========================================
Relatório de Análise de Senha
========================================
Tamanho OK: ✔
Tem Número: ✔
Tem Maiúscula: ✔
Tem Minúscula: ✔
Tem Especial: ✔
Não é Comum: ✔
----------------------------------------
Pontuação: 6/6
Entropia estimada: 65.2 bits
Força: Senha Forte
Status: SENHA APROVADA
========================================
🗺️ Possíveis melhorias futuras
 Adicionar testes automatizados com pytest
 Carregar a lista de senhas comuns de um arquivo externo (wordlist maior)
 Criar uma interface de linha de comando com argparse (ex: --min-length, --json)
 Expor uma função reutilizável como biblioteca (não só via terminal)
 Adicionar integração contínua (GitHub Actions) rodando testes e lint a cada push

👩‍💻 Autora

Desenvolvido por VitoriaChuarts como projeto de estudo em cibersegurança.
