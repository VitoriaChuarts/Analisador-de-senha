import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from password_audit import PasswordAuditor, ResultadoAnaliseSenha, SENHAS_COMUNS, CARACTERES_ESPECIAIS

def test_senha_curta_reprovada()
    auditor = PasswordAuditor(tamanho_minimo=8)
    resultado = auditor.analisar_senha("abc")
    assert resultado.tamanho_ok == False
    assert resultado.aprovado == False

def test_senha_comum_reprovada():
    auditor = PasswordAuditor(tamanho_minimo=8)
    resultado = auditor.analisar_senha("12345678")
    assert resultado.nao_e_comum == False
    assert resultado.classificacao == "Senha Comum"

def test_senha_forte_aprovada():
    auditor = PasswordAuditor(tamanho_minimo=8)
    resultado = auditor.analisar_senha("Abcdef1!")
    assert resultado.aprovado == True
    assert resultado.classificacao == "Senha Forte"

def test_entropia_0_se_estiver_vazia():
    auditor = PasswordAuditor(tamanho_minimo=8)
    resultado = auditor.analisar_senha("")
    assert resultado.entropia_bits == 0

    