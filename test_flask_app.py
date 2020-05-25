import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase):#importar de testflaskbase para ejecutar los métodos contenidos dentro
    def test_server_is_on(self):
        loquemedevuelve = self.client.get("/")#petición get para comprobar ruta /
        self.assertEqual(loquemedevuelve.status_code, 200)#comprobar la respuesta del test debe ser 200

    def test_root_index_is_Hola_mundo(self):
        loquemedevuelve = self.client.get("/")#petición get para comprobar ruta /
        self.assertEqual(loquemedevuelve.status_code, 200)#comprobar la respuesta del test debe ser 200
        self.assertEqual(loquemedevuelve.data, b"Hola mundo")#comprobar que en index hay "Hola mundo"




if __name__ == "__main__":
    unittest.main()