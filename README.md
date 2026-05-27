# 🏦 Sistema Bancário
 
Simulador simples de operações bancárias em Python, com suporte a depósitos, saques e extrato.
 
## Funcionalidades
 
- **Depósito** — adiciona valor ao saldo da conta
- **Saque** — retira valor com limite de R$500 por operação e máximo de 3 saques por sessão
- **Extrato** — exibe saldo atual, número de depósitos e valores depositados
- **Sair** — encerra o sistema
## Como executar
 
```bash
python Sistema_bancario.py
```
 
## Regras de negócio
 
- Saldo inicial: **R$ 3.000,00**
- Limite por saque: **R$ 500,00**
- Máximo de saques por sessão: **3**
- Não são permitidos depósitos ou saques com valor zero ou negativo
## Exemplo de uso
 
```
[S]-Saque [D]-Depósito [E]-extrato [Q]-Sair: D
Digite um valor para depósito: 200
Depósito: 200.00
Valor na conta: 3200.00
 
[S]-Saque [D]-Depósito [E]-extrato [Q]-Sair: S
Digite um Valor de retirada: 150
Valor R$150.00 Retirado com Sucesso
Seu saldo é de 3050.00
```
 
## Tecnologias
 
- Python 3.10+ (utiliza `match/case`)



