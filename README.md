# eCommerceBackend

**Requirements**

- Python 3.8.5
- PostgreSQL 12.5
- All packages in *requirements.txt*

**PostgreSQL Setup**

1. `sudo apt install python-pip python-dev libpq-dev postgresql-12 postgresql-contrib`
2. `sudo su - postgres`
3. `psql`
4. `CREATE DATABASE your_db_name;`
5. `CREATE USER your_user_name WITH PASSWORD 'your_password';`
6. `ALTER ROLE your_user_name SET client_encoding TO 'utf8';`
7. `ALTER ROLE your_user_name SET default_transaction_isolation TO 'read committed';`
8. `ALTER ROLE your_user_name SET timezone TO 'UTC';`
9. `GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_user_name;`
10. `\q`
11. `exit`

**Virtualenv Setup**

1. `python3 -m venv your_env_name`
2. `. your_env_name/bin/activate`
3. `pip install -r requirements.txt`

**Note:** Care about where you set *your_env_name*