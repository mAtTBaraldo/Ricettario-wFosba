import mysql.connector

#connessione ad un database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "ricettario"
)

#collegamento cursore 
cursor = db.cursor()

cursor.execute("CREATE TABLE ricettario (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")