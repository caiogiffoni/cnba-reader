<h1 align="center">
  CNBA - Reader - Django
</h1>

## 💻 Projeto

API para upload de arquivos no formato CNBA e visualização das tabelas por estabelecimentos

## 🔨 Implementações

- [x] Upload de arquivo e persistência no banco de dados
- [x] Páginas templates no Django
- [x] Testes
- [x] Docker
- [ ] Heroku

## ✨ Tecnologias

- [x] Django
- [x] Django Rest Framework
- [x] Docker / Docker compose

## 🌐 Deploy

#### Sem deploy por enquanto

[Link do deploy]()

## Quick Start - BackEnd

### 1.1. Clonando o repositório

Clone o repositório na sua máquina

### 1.2. Variáveis de ambiente

Crie um arquivo **.env**, copiando o exemplo **.env.example**.
Configure conforme credenciais do Postgres.

### 1.3. Vá a pasta e rode o Docker
*Necessário ter docker instalado

rode:

```

docker compose up

```

### 1.4. Vá ao terminal


rode:

```
docker exec -it cnba-reader-web-1 bash
```

e dentro do terminal bash do docker, rode:

```
python manage.py generate_transactions
```

### 1.5. Use a aplicação em:

http://localhost:8000/home/

e faça upload do seu arquivo CNBA
