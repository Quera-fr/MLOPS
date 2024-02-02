# Construction de l'image docker et push sur Heroku
docker buildx build --platform linux/amd64 -t streamlit_isen  .

# Construction de l'image docker et push sur Heroku
#docker build . -t streamlit_isen

# Tag de l'image au registre Heroku
docker tag streamlit_isen registry.heroku.com/streamlit-isen-kevin/web

# Push de l'image sur Heroku
docker push registry.heroku.com/streamlit-isen-kevin/web              

# Lancement de l'application
heroku container:release web -a streamlit-isen-kevin                  