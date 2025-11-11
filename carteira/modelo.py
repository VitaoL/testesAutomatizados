from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class TipoTransacao(str, Enum):
    DEPOSITO = "deposito"
    SAQUE = "saque"


@dataclass(slots=True)
class Transacao:
    """Representa uma movimentação financeira na carteira."""

    valor: float
    tipo: TipoTransacao
    descricao: str
    data: datetime = field(default_factory=datetime.utcnow)
    identificador: Optional[str] = None

    def __post_init__(self) -> None:
        self.validar()

    def validar(self) -> None:
        if self.valor <= 0:
            raise ValueError("O valor da transação deve ser positivo")

        if not isinstance(self.tipo, TipoTransacao):
            raise TypeError("Tipo de transação inválido")

        if not self.descricao.strip():
            raise ValueError("Descrição não pode ser vazia")

    @property
    def eh_deposito(self) -> bool:
        return self.tipo is TipoTransacao.DEPOSITO

    @property
    def eh_saque(self) -> bool:
        return self.tipo is TipoTransacao.SAQUE

    def aplicar(self, saldo_atual: float) -> float:
        if self.eh_deposito:
            return saldo_atual + self.valor

        if self.valor > saldo_atual:
            raise ValueError("Saldo insuficiente para realizar saque")

        return saldo_atual - self.valor
