import pytest

from carteira.modelo import TipoTransacao
from carteira.repositorio import RepositorioTransacao
from carteira.servico import ServicoCarteira


def criar_servico() -> ServicoCarteira:
    return ServicoCarteira(repositorio=RepositorioTransacao())


def registrar_transacoes_iniciais(servico: ServicoCarteira) -> None:
    servico.registrar_deposito(100.0, "Depósito inicial")
    servico.registrar_deposito(50.0, "Bônus")


def test_registrar_deposito_atualiza_saldo():
    servico = criar_servico()
    servico.registrar_deposito(100.0, "Depósito inicial")

    saldo = servico.calcular_saldo()

    assert saldo == pytest.approx(100.0)


def test_registrar_saque_valida_saldo_disponivel():
    servico = criar_servico()
    registrar_transacoes_iniciais(servico)

    servico.registrar_saque(80.0, "Retirada")

    assert servico.calcular_saldo() == pytest.approx(70.0)


def test_registrar_saque_sem_saldo_dispara_excecao():
    servico = criar_servico()
    servico.registrar_deposito(30.0, "Depósito inicial")

    with pytest.raises(ValueError):
        servico.registrar_saque(100.0, "Compra")


def test_historico_retorna_transacoes_em_ordem_de_registro():
    servico = criar_servico()
    registrar_transacoes_iniciais(servico)

    historico = list(servico.historico())

    assert len(historico) == 2
    assert all(transacao.tipo is TipoTransacao.DEPOSITO for transacao in historico)
