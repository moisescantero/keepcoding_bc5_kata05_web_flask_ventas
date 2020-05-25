from flask import Flask
from flask_testing import TestCase
import run

class TestFlaskBase(TestCase):#clase para crear la base de nuestro test comprueba conexión a servidor
    def create_app(self):
        self.app = run.app#guardar app en atributo de clase
        return run.app#devolver sí o sí la app

    
    def setUp(self):
        self.client = self.app.test_client()#crear cliente de testing
        self.client.testing = True#decir que es cliente de pruebas o testing

    def tearDown(self):
        pass
