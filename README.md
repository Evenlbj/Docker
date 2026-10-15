# Serveur web Docker

Exercice : construire une image Docker qui lance un serveur web Python avec Flask.

## Fichiers

- `Dockerfile` : instructions de construction de l'image.
- `app.py` : application web Flask.
- `requirements.txt` : dépendances Python.

## Construire l'image

Depuis ce dossier :

```bash
docker build -t mon-serveur-web .
```

## Lancer le conteneur

```bash
docker run -it --rm --name my_webserver -p 9000:9000 mon-serveur-web
```

Ouvrir ensuite http://localhost:9000 dans un navigateur.

## Instructions Docker utilisées

- `FROM` : image Python de base.
- `COPY` : copie les fichiers dans l'image.
- `RUN` : installe Flask pendant le build.
- `EXPOSE` : documente le port 9000 utilisé par l'application.
- `CMD` : démarre le serveur web.
