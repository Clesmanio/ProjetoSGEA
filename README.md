# Sistema de Gestão de Eventos Acadêmicos (SGEA)

O SGEA é um sistema web desenvolvido em **Django** para o gerenciamento de eventos acadêmicos, com foco em **segurança**, **regras de negócio estritas** e **boas práticas de backend**.

### Objetivo e Destaques

O projeto cumpre todos os requisitos acadêmicos, destacando:
1.  **Segurança por Perfil:** Acesso restrito a funcionalidades críticas (criação/edição/deleção de eventos) apenas para o perfil **Organizador Proprietário**.
2.  **Modelagem de Dados:** Estrutura `Usuario`, `Evento`, e `Inscricao` com controle de vagas e status de certificado.
3.  **Interface Limpa:** Templates totalmente migrados e limpos de classes antigas de projetos desenvolvido em sala.
4.  **Autenticação Segura:** Uso de **E-MAIL** como login único e obrigatório.

### Funcionalidades Chave

* **Autenticação:** Login/Logout e Cadastro de Usuários (Organizador, Aluno, Professor).
* **Gerenciamento de Eventos (CRUD):** Protegido, permitindo edição apenas ao organizador criador.
* **Inscrição:** Controle de vagas e impedimento de inscrições duplicadas.
* **Cancelamento:** Permite ao usuário remover a própria inscrição.
* **Certificados:** Controle do status de emissão por evento.

## 🛠️ Tecnologias e Configuração

* **Backend:** Python, Django
* **Frontend:** HTML/CSS (Protótipo)
* **Banco de Dados:** SQLite

### Instalação e Execução

1.  Clone o repositório e ative o ambiente virtual.
2.  Instale as dependências: `pip install django`.
3.  Aplique as migrações (criação final das tabelas): `python manage.py makemigrations` e `python manage.py migrate`.
4.  **População Segura:** Certifique-se de que o arquivo **`populate_secure.py`** está na raiz do projeto.
5.  **Execute o script de população** para inserir os 58 usuários de teste (senha `123456`):
    ```bash
    python populate_secure.py
    ```
6.  Inicie o servidor: `python manage.py runserver`.

###  Credenciais de Teste

O login é feito usando o **E-mail** e a senha padrão **`123456`**.

| Perfil | Usuário de Login (E-mail) | Senha |
| :--- | :--- | :--- |
| **ORGANIZADOR** | `ana@ceub.edu` | `123456` |
| **ALUNO** | `felipe@aluno.com` | `123456` |

---

### Equipe de Desenvolvimento

| Integrante | Matrícula |
| :--- | :--- |
| Clesmanio Filho | 22407802 |
| Eduardo Martins | 22403813 |
| João Vitor Passos | 22404386 |
