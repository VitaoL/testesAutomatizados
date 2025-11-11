# Relatório da Atividade de Testes Automatizados

## 🎯 Objetivo
Implementar testes automatizados que assegurem o correto funcionamento das principais regras de negócio e operações do sistema de carteira digital.

## 🧪 Testes Implementados
Os testes foram desenvolvidos com **pytest** e cobrem diferentes camadas do sistema.

### 1. Camada de Domínio (`carteira/modelo.py`)
- `test_transacao_deposito_aumenta_saldo`
- `test_transacao_saque_valida_saldo_insuficiente`
- `test_transacao_valor_negativo_dispara_excecao`
- `test_transacao_descricao_invalida`

Esses testes verificam a validação de valores, descrição e regras de aplicação de saldo da classe `Transacao`.

### 2. Camada de Persistência (`carteira/repositorio.py`)
- `test_salvar_transacao_sem_identificador_retorna_erro`
- `test_salvar_e_obter_transacao`
- `test_listar_transacoes_retorna_lista_completa`

Validam o comportamento do repositório em memória responsável por armazenar e recuperar transações.

### 3. Camada de Serviços (`carteira/servico.py`)
- `test_registrar_deposito_atualiza_saldo`
- `test_registrar_saque_valida_saldo_disponivel`
- `test_registrar_saque_sem_saldo_dispara_excecao`
- `test_historico_retorna_transacoes_em_ordem_de_registro`

Asseguram que o serviço de carteira registra transações corretamente, mantém o saldo atualizado e valida operações inválidas.

## ▶️ Como executar os testes
Com o Python 3.10+ instalado, execute:

```bash
pip install -r requirements.txt
pytest
```

## 🔗 Repositório
<https://github.com/usuario/testesAutomatizados>
