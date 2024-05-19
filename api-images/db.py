import mysql.connector

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="database-proyecto.c45ddxrq8nnm.us-east-1.rds.amazonaws.com",
    user="admin",
    password="database-proyecto",
    database="imagenes"
)

cursor = conn.cursor()

# Consulta SQL para crear la tabla images en MySQL
sql_query = """
CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(250) NOT NULL,
    url VARCHAR(250) NOT NULL
)
"""

# Ejecutar la consulta
cursor.execute(sql_query)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
