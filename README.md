# Gerenciador de Saldo de Contas

Este é um aplicativo para gerenciamento de saldo de contas, construído usando Flask, um framework web em Python. Ele fornece uma API RESTful para realizar operações como depósito, saque e transferência de fundos entre contas. Os usuários podem interagir com o sistema através de requisições HTTP, permitindo-lhes criar contas, depositar e retirar fundos, bem como transferir dinheiro entre contas. O aplicativo também oferece endpoints para verificar o saldo das contas e redefinir o estado do sistema para fins de teste. Seu código-fonte é modular e bem estruturado, facilitando a expansão e manutenção futuras.

## Como usar

1. Instale as dependências usando o comando `pip install -r requirements.txt`.
2. Execute o aplicativo usando o comando `python -m app.main`.
3. Acesse os endpoints da API conforme documentado abaixo.

## Endpoints da API

- **Resetar o Estado**: `POST /reset` - Reseta o estado do sistema.
- **Obter Saldo**: `GET /balance?account_id=ID` - Retorna o saldo da conta com o ID especificado.
- **Processar Evento**: `POST /event` - Processa um evento que altera o saldo de uma conta.
  - Corpo da Requisição:
    ```json
    {
      "type": "deposit" | "withdraw" | "transfer",
      "destination": "account_id",  // obrigatório para "deposit" e "transfer"
      "origin": "account_id",       // obrigatório para "withdraw" e "transfer"
      "amount": number
    }
    ```
  
## Como Testar

Você pode usar ferramentas como [Postman](https://www.postman.com/) para enviar requisições HTTP para os endpoints da API e verificar as respostas.

## Notas

- Certifique-se de que o servidor está em execução antes de enviar requisições. Use `python -m app.main` para iniciar o servidor.
- Este projeto é parte do processo seletivo para a vaga de engenheiro de software na EBANX.

