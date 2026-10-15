from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
    <!doctype html>
    <html lang="fr">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Mon serveur web Docker</title>
      </head>
      <body>
        <h1>Mon serveur web Docker</h1>
        <p>Mon serveur fonctionne correctement !</p>
        <p>Projet réalisé avec Python, Flask et Docker.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
