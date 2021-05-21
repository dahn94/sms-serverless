# sms-serverless
Serviço web que envia sms por meio do Twilio construído com o framework Chalice e deploy no AWS Lambda

<h2> Configuração necessária para rodar o projeto</h2>

1. Após clonar o repositório em seu computador, mova-se para dentro da pasta do projeto e realize a criação de ambiente virtual para rodar a aplicação:
```
python3 -m venv nome_da_virtualenv
```

2. Ative a máquina virtual
```
.\nome_da_virtualenv\Scripts\activate (CMD/PowerShell) 
source /nome_da_virtualenv/bin/activate (bash/zsh)
```

3. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

4. Adicione as configurações (Account Sid, Auth Token e Phone Number) encontradas no Project Info do Twilio:

```
.chalice/config.json
```

5. Realize o Deploy na AWS Lambda (Certifique-se que suas credenciais estão gravadas no seu diretório inicial):
```
chalice deploy
```

6. Fazendo uma requisição:
```
$ curl -H "Content-Type: application/json" -X POST -d '{"msg": "Olá, Mundo!!!"}' Sua_Rest_API_URL+/service/sms/send
```
