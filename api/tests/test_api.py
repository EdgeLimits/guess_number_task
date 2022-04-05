from rest_framework import status
from rest_framework.test import APITestCase


# https://github.com/encode/django-rest-framework/blob/master/tests/test_serializer.py

class TestGuessView(APITestCase):
    def test_action_start(self):
        data = {
            "action": "start"
        }

        response = self.client.post(
            path="/",
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_no_action(self):
        data = {
        }

        response = self.client.post(
            path="/",
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_wrong_action_start(self):
        data = {
            "action": "starts"
        }

        response = self.client.post(
            path="/",
            data=data,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
