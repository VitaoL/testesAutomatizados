# Testes Automatizados - Carteira Digital

Este repositório contém um exemplo de aplicação simples de carteira digital desenvolvido para a disciplina de Testes Automatizados. O foco é demonstrar a implementação de testes nas camadas de domínio, persistência e serviços utilizando **pytest**.

## Estrutura do projeto

```
carteira/
├── modelo.py          # Entidades e regras de domínio
├── repositorio.py     # Persistência em memória
└── servico.py         # Casos de uso da carteira

ENTREGA.md             # Relatório da atividade
requirements.txt       # Dependências para execução dos testes
tests/                 # Conjunto de testes automatizados
```

## Como executar

1. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Rode a suíte de testes:
   ```bash
   pytest
   ```

Consulte o arquivo [ENTREGA.md](ENTREGA.md) para mais detalhes sobre os testes implementados.
