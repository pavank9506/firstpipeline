import unittest
from app import app  # Import the Flask app from your main application file

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode

    def test_welcome(self):
        # Send a GET request to the root URL
        response = self.app.get('/')
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the response JSON contains the expected message
        self.assertEqual(response.get_json(), {"message": "You are welcome!"})

if __name__ == '__main__':
    unittest.main()
 