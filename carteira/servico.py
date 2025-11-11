from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
from uuid import uuid4

from .modelo import TipoTransacao, Transacao
from .repositorio import RepositorioTransacao


@dataclass
class ServicoCarteira:
    repositorio: RepositorioTransacao

    def registrar_deposito(self, valor: float, descricao: str) -> Transacao:
        transacao = Transacao(valor=valor, tipo=TipoTransacao.DEPOSITO, descricao=descricao)
        transacao.identificador = uuid4().hex
        return self.repositorio.salvar(transacao)

    def registrar_saque(self, valor: float, descricao: str) -> Transacao:
        transacao = Transacao(valor=valor, tipo=TipoTransacao.SAQUE, descricao=descricao)
        transacao.identificador = uuid4().hex

        saldo_atual = self.calcular_saldo()
        transacao.aplicar(saldo_atual)

        return self.repositorio.salvar(transacao)

    def calcular_saldo(self) -> float:
        saldo = 0.0
        for transacao in self.repositorio.listar():
            saldo = transacao.aplicar(saldo)
        return saldo

    def historico(self) -> Iterable[Transacao]:
        return self.repositorio.listar()
