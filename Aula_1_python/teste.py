import psycopg2

# Substitua os valores pelos dados do seu banco de dados
database_name = "Strong_conv"
user = "postgres"
password = "Strong123@"
host = "localhost"  # Ou o endereço IP do servidor PostgreSQL
port = "5432"       # Porta padrão do PostgreSQL

try:
    connection = psycopg2.connect(
        database=database_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Conexão estabelecida com sucesso!")

    # Aqui você pode executar operações no banco de dados usando a conexão e o cursor

    connection.close()
    print("Conexão encerrada.")
except psycopg2.Error as e:
    print("Erro ao conectar:", e)