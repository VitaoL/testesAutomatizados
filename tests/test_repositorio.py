import pytest

from carteira.modelo import TipoTransacao, Transacao
from carteira.repositorio import RepositorioTransacao


def criar_transacao(identificador: str = "abc123") -> Transacao:
    transacao = Transacao(valor=50.0, tipo=TipoTransacao.DEPOSITO, descricao="Teste")
    transacao.identificador = identificador
    return transacao


def test_salvar_transacao_sem_identificador_retorna_erro():
    repositorio = RepositorioTransacao()
    transacao = Transacao(valor=20.0, tipo=TipoTransacao.DEPOSITO, descricao="Teste")
    with pytest.raises(ValueError):
        repositorio.salvar(transacao)


def test_salvar_e_obter_transacao():
    repositorio = RepositorioTransacao()
    transacao = criar_transacao()

    repositorio.salvar(transacao)
    obtida = repositorio.obter("abc123")

    assert obtida is transacao


def test_listar_transacoes_retorna_lista_completa():
    repositorio = RepositorioTransacao()
    transacoes = [criar_transacao("id1"), criar_transacao("id2")]

    for transacao in transacoes:
        repositorio.salvar(transacao)

    assert list(repositorio.listar()) == transacoes
