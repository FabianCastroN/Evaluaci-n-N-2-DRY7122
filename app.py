from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡Aplicación de muestra funcionando en el puerto 9999!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)
