from django.test import TestCase
from destinations.models import Destination
import json

class DestinationGraphQLTest(TestCase):

    def setUp(self):
        Destination.objects.create(
            name="برج میلاد",
            city="تهران",
            description="نماد تهران",
            price=0
        )

    def test_all_destinations(self):
        query = """
        query {
          allDestinations {
            id
            name
            city
            price
          }
        }
        """

        response = self.client.post(
            "/graphql/",
            data=json.dumps({"query": query}),
            content_type="application/json"
        )

        content = response.json()

        self.assertNotIn("errors", content)
        self.assertEqual(len(content["data"]["allDestinations"]), 1)
        self.assertEqual(content["data"]["allDestinations"][0]["name"], "برج میلاد")
