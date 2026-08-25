import os

from flask import Flask, jsonify
from dotenv import load_dotenv
import psycopg2

load_dotenv()
app = Flask(__name__)

def get_connection():
     return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.route("/choferes", methods=["GET"])
def obtener_choferes():
     conexion = get_connection()
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM choferes;")
     resultados = cursor.fetchall()
     cursor.close()
     conexion.close()
     return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)