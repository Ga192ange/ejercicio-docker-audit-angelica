import os

from flask import Flask, request

app = Flask(__name__)

# Credenciales obtenidas mediante variables de entorno
DB_HOST = os.getenv("DB_HOST", "servidor-bd-ejemplo")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME", "legacydb")


@app.route("/")
def home():
    try:
        # La conexión a la BD se mantiene simulada para este ejercicio
        return "<h1>API Legacy TechNova - Funcionando</h1>"
    except Exception as e:
        return f"<h1>Sistema Caído</h1><p>{e}</p>", 500


@app.route("/buscar")
def buscar_usuario():
    usuario_id = request.args.get("id", "1")

    # Validación del identificador recibido por el usuario
    if not usuario_id.isdigit():
        return "El ID debe ser un número entero", 400

    # Consulta preparada con parámetro
    query = "SELECT * FROM usuarios WHERE id = %s"

    return f"Consulta preparada: {query} | Parámetro: {usuario_id}"


@app.route("/health")
def health_check():
    # El endpoint de salud debe responder de forma estable
    return "OK", 200


if __name__ == "__main__":
    app.run(
    host=os.getenv("HOST", "0.0.0.0"),  # nosec B104 - Necesario para exponer el servicio fuera del contenedor Docker; el acceso se restringe vía red de Docker/firewall del host
    port=int(os.getenv("PORT", "5050")),
    debug=False
)