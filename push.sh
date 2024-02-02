#heroku create isen-brest-mlflow
#access:add aaddresse@mail.com --app=isen-brest-mlflow

heroku container:login

# Construction de l'image Docker
docker buildx build --platform linux/amd64 -t isen-brest-mlflow .
#docker build -t isen-brest-mlflow .

# Tag de l'image Docker à Heroku (IMAGE - APPLICATION Heroku)
docker tag isen-brest-mlflow registry.heroku.com/isen-brest-mlflow/web

# Push de l'image Docker
docker push registry.heroku.com/isen-brest-mlflow/web

# Release de l'image Docker
heroku container:release web -a isen-brest-mlflow

# Ouverture de l'application
heroku open -a isen-brest-mlflow

# Logs de l'application
heroku logs --app=isen-brest-mlflow --tail 