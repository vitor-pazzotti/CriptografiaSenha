import unittest
from CriptografiaSenha import hash_md5
from CriptografiaSenha import hash_sha256

class TesteCriptografia(unittest.TestCase):
    def diferenca_espaco_md5(self):
        self.assertNotEqual(hash_md5('teste'), hash_md5('teste '),msg=None)
    
    def diferenca_espaco_sha256(self):
        self.assertNotEqual(hash_sha256('teste'), hash_sha256('teste '),msg=None)
        
    def diferenca_md5_sha256(self):
        self.assertNotEqual(hash_md5('teste'), hash_sha256('teste'),msg=None)
    
    def vazio_md5(self):
        self.assertEqual(hash_md5(''),'d41d8cd98f00b204e9800998ecf8427e')

    def vazio_sha256(self):
        self.assertEqual(hash_sha256(''),'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

if __name__ == "__main__":
    unittest.main()