from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .modelo import Transacao


@dataclass
class RepositorioTransacao:
    """Armazena transações em memória para simplificar os testes."""

    _transacoes: Dict[str, Transacao] = field(default_factory=dict)

    def salvar(self, transacao: Transacao) -> Transacao:
        if transacao.identificador is None:
            raise ValueError("Transação deve possuir identificador antes de ser salva")

        self._transacoes[transacao.identificador] = transacao
        return transacao

    def obter(self, identificador: str) -> Optional[Transacao]:
        return self._transacoes.get(identificador)

    def listar(self) -> Iterable[Transacao]:
        return list(self._transacoes.values())

    def limpar(self) -> None:
        self._transacoes.clear()
