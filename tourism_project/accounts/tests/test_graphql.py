from django.test import TestCase
from django.contrib.auth.models import User
import json

class UserGraphQLTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="123456"
        )

    def test_all_users_query(self):
        query = """
        query {
          allUsers {
            id
            username
            email
          }
        }
        """

        response = self.client.post(
            "/graphql/",
            data=json.dumps({"query": query}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        content = response.json()

        self.assertNotIn("errors", content)
        self.assertEqual(len(content["data"]["allUsers"]), 1)
        self.assertEqual(content["data"]["allUsers"][0]["username"], "testuser")
