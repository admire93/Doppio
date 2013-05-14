import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
