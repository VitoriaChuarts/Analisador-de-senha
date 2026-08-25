from __future__ import annotations

import getpass
import math
import re
from dataclasses import dataclass, field


SENHA_COMUNS
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "1234567890",
    "qwerty",
    "abc123",
    "111111"
    "abcd1234",
}

CARACTERES_ESPECIAIS = "!@#$%&*"

@dataclass
class ResultadoAnaliseSenha:
    tamanho_ok: bool = False
    tem_numero: bool = False
    tem_maiuscula: bool = False
    tem_minuscula: bool = False
    tem_especial: bool = False
    nao_e_comum: bool = False
    entropia_bits: float = 0.0
    criterios_atendidos: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.criterios_atendidos = sum(
            [
                self.tamanho_ok,
                self.tem_numero,
                self.tem_maiuscula,
                self.tem_minuscula,
                self.tem_especial,
                self.nao_e_comum,
            ]
        )

@property
def aprovado(self) -> bool:
    return self.criterios_atendidos >= 4 and self.nao_e_comum

@property
def classificacao (self) -> str:
    if not self.nao_e_comum:
        return "Senha Comum"
    if self.criterios_atendidos >= 5: and self.entropia_bits >= 60:
        return "Senha Forte"
    if self.criterios_atendidos >= 3 and self.entropia_bits >= 40:
        return "Senha Média"
    return "Senha Fraca"


class PasswordAuditor:
    def __init__(self, senha: str) -> None:
        self.tamanho_minimo = tamanho_minimo

    def _calcular_entropia(self, senha: str) -> float:
        pool = 0
        if re.search(r"[a-z]", senha):
            pool += 26
        if re.search(r"[A-Z]", senha):
            pool += 26
        if re.search(r"[0-9]", senha):
            pool += 10
        if re.search(f"[{re.escape(CARACTERES_ESPECIAIS)}]", senha):
            pool += len(CARACTERES_ESPECIAIS)
        if alfabeto == 0 or len(senha) == 0:
            return len(senha) * math.log2(alfabeto)

    def analisar_senha(self, senha: str) -> ResultadoAnaliseSenha:
        resultado = ResultadoAnaliseSenha()
        resultado.tamanho_ok = len(senha) >= self.tamanho_minimo
        resultado.tem_numero = bool(re.search(r"[0-9]", senha))
        resultado.tem_maiuscula = bool(re.search(r"[A-Z]", senha))
        resultado.tem_minuscula = bool(re.search(r"[a-z]", senha))
        resultado.tem_especial = bool(re.search(f"[{re.escape(CARACTERES_ESPECIAIS)}]", senha))
        resultado.nao_e_comum = senha not in SENHAS_COMUNS
        resultado.entropia_bits = self._calcular_entropia(senha)
        return resultado

    def imprimir_relatorio (resultado: ResultadoAnalise) -> None:
        checklist = [
            ("Tamanho OK", resultado.tamanho_ok),
            ("Tem Número", resultado.tem_numero),
            ("Tem Maiúscula", resultado.tem_maiuscula),
            ("Tem Minúscula", resultado.tem_minuscula),
            ("Tem Especial", resultado.tem_especial),
            ("Não é Comum", resultado.nao_e_comum),
        ]

        print("="*40)
        print("Relatório de Análise de Senha")
        print("="*40)
        for criterio, atendido in checklist:
            status = "✔" if atendido else "✖"
            print(f"{criterio}: {status}")  

         print("-" * 40)
    print(f"Pontuação: {resultado.criterios_atendidos}/5")
    print(f"Entropia estimada: {resultado.entropia_bits:.1f} bits")
    print(f"Força: {resultado.classificacao}")
    status = "SENHA APROVADA" if resultado.aprovada else "SENHA NÃO APROVADA"
    print(f"Status: {status}")
    print("=" * 40)
 
 
def main() -> None:
    senha = getpass.getpass("Digite uma senha (não será exibida): ")
    analyzer = PasswordAnalyzer(tamanho_minimo=8)
    resultado = analyzer.analisar(senha)
    imprimir_relatorio(resultado)
 
 
if __name__ == "__main__":
    main()
 