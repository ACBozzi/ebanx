import unittest

from app import create_app
from app.controllers.balance_controller import balance_bp


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()