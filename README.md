# BigData

### Download:

```bash
$ git clone https://github.com/dyegocaldeira/bigdata
$ cd bigdata
```

### Requisitos
```bash
$ pip3 install -r requirements.txt
```

Após isso, será necessário criar as váriaveis de ambiente no diretório da aplicação com os dados da conexão RDS. Ex:
```bash
$ touch .env
```

### ENV:
```env
HOST='host-aws'
USERDB='user-db'
PASSDB='pass-db'
DB='db-name'
```

### Utilização

Deve ter o arquivo `access.csv` no mesmo diretório da aplicação
```bash
$ python3 app-rds.py
```
