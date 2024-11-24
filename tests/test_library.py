import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from library import generate_id, load_library

class TestLibraryManager(unittest.TestCase):
    def test_generate_id(self):
        library = [{"id": 1}, {"id": 2}, {"id": 3}]
        self.assertEqual(generate_id(library), 4)

    def test_load_library_empty(self):
        self.assertEqual(load_library(), [])

if __name__ == "__main__":
    unittest.main()