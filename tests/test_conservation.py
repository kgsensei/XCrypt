import os
import random
import string
import unittest
import xcrypt

class MyTestCase(unittest.TestCase):
    def test_conservation(self):
        key=xcrypt.make_key()
        for _ in range(100):
            seq=''.join(random.choice(string.hexdigits)for _ in range(500))
            enc:str=xcrypt.encrypt(key,seq)
            self.assertEqual(xcrypt.decrypt(key,enc),seq)

    @classmethod
    def tearDownClass(cls)->None:
        for file in os.listdir('.'):
            if file.endswith('.key'):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()
