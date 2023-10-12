import unittest
import app

class TestApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(app.add(2, 3), 5)
    pass

if __name__ == '__main__':
    unittest.main()
    
    