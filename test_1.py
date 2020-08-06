#Importar Librerías
import unittest
import moduloTest

#Clase que permite hacer un test unitario de la función test 1
class TestMyModule(unittest.TestCase):

    def test_1(self):
        self.assertEqual(moduloTest.Test1(), 1)

#Si el resultado del test es igual a 1 el método unittest.main() restorna el tiempo de ejecución del test
#si no retorna un error
if __name__ == "__main__":
   unittest.main()