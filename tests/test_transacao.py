import pytest

from carteira.modelo import TipoTransacao, Transacao


def test_transacao_deposito_aumenta_saldo():
    transacao = Transacao(valor=100.0, tipo=TipoTransacao.DEPOSITO, descricao="Pagamento")
    saldo_final = transacao.aplicar(50.0)
    assert saldo_final == pytest.approx(150.0)


def test_transacao_saque_valida_saldo_insuficiente():
    transacao = Transacao(valor=200.0, tipo=TipoTransacao.SAQUE, descricao="Pagamento de conta")
    with pytest.raises(ValueError):
        transacao.aplicar(150.0)


def test_transacao_valor_negativo_dispara_excecao():
    with pytest.raises(ValueError):
        Transacao(valor=-10.0, tipo=TipoTransacao.DEPOSITO, descricao="Erro")


@pytest.mark.parametrize("descricao", ["   ", ""])
def test_transacao_descricao_invalida(descricao: str):
    with pytest.raises(ValueError):
        Transacao(valor=10.0, tipo=TipoTransacao.DEPOSITO, descricao=descricao)
