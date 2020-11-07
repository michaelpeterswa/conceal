import unittest
import conceal


class TestConfigLoader(unittest.TestCase):
    def test_load(self):
        conf = conceal.config("conceal.toml")
        self.assertIsInstance(conf, dict)


if __name__ == "__main__":
    unittest.main()
