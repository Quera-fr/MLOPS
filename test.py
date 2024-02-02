# Import des librairies
from unittest import TestCase, main
from fastapi.testclient import TestClient
from api import app

# Tests unitaire de l'environnement de développement
class TestDev(TestCase):

    # Vérifie que les fichiers sont présents
    def test_files(self):
        import os
        list_files = os.listdir()
        self.assertIn("api.py", list_files)
        self.assertIn("requirements.txt", list_files)
        self.assertIn(".gitignore", list_files)
        self.assertIn("utiles", list_files)
        

        # Vérifie que le fichier data.csv est présent dans le dossier utiles
        list_files = os.listdir("utiles")
        self.assertIn("data.csv", list_files)
        self.assertIn("model.pkl", list_files)

     

    # Vérifie que les requirements sont présents
    def test_requirements(self):
        with open("requirements.txt", "r") as f:
            requirements = f.read()
        self.assertIn("uvicorn", requirements)
        self.assertIn("fastapi", requirements)
        self.assertIn("scikit-learn==1.3.1", requirements)
        self.assertIn("pandas==2.0.3", requirements)
        self.assertIn("httpx", requirements)
        self.assertIn("pydantic", requirements)
        self.assertIn("python-multipart", requirements)
    

    # Vérifie que le gitignore est présent
    def test_gitignore(self):
        with open(".gitignore", "r") as f:
            gitignore = f.read()
        self.assertIn("__pycache__", gitignore)
        self.assertIn(".vscode", gitignore)

    

# Création du client de test
client = TestClient(app)

# Tests unitaire de l'API
class TestApi(TestCase):
    
    # Vérifie que l'API est bien lancée
    def test_api(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World!!!"})

    
    # Vérifie que l'API est bien lancée
    def test_api(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World!!!"})
    

    # Vérifie le endpoint hello_you
    def test_hello_you(self):
        response = client.get("/hello?name=John")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello John"})
    

    # Vérifie le endpoint predict
    def test_predict(self):
        data = {'age': 58,
                'job': 1,
                'marital': 1,
                'education': 2,
                'default': 0,
                'balance': 2143,
                'housing': 1,
                'loan': 0,
                'campaign': 1,
                'pdays': -1,
                'previous': 0,
                'poutcome': 3
            }
        response = client.post("/predict-local", json=data)
        self.assertEqual(response.status_code, 200)




# Test du modèle individuellement
#class TestModel(TestCase):

    # Vérifie que le modèle est bien présent
    

    # Vérifie que le modèle est bien chargé
    

    # Vérifie que le modèle est bien chargé
    

# Démarrage des tests
if __name__ == '__main__':

    main(
        verbosity=2,
    )




# assertEqual(a, b) : Vérifie si a est égal à b.
# assertNotEqual(a, b) : Vérifie si a est différent de b.
        
# assertIn(a, b) : Vérifie si a est dans b.
# assertNotIn(a, b) : Vérifie si a n'est pas dans b.
        
# assertIs(a, b) : Vérifie si a est b.
# assertIsNot(a, b) : Vérifie si a n'est pas b.
        
# assertTrue(x) : Vérifie si x est vrai.
# assertFalse(x) : Vérifie si x est faux.
        
# assertIsNone(x) : Vérifie si x est None.
# assertIsNotNone(x) : Vérifie si x n'est pas None.
        
# assertIsInstance(a, b) : Vérifie si a est une instance de b.
# assertNotIsInstance(a, b) : Vérifie si a n'est pas une instance de b.
        
# assertRaises(exc, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc.
# assertRaisesRegex(exc, r, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc et dont le message correspond à l'expression régulière r.
