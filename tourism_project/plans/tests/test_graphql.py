from django.test import TestCase
from django.contrib.auth.models import User
from destinations.models import Destination
from plans.models import Plan
import json

class PlanGraphQLTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="masoud",
            email="masoud@test.com",
            password="123456"
        )

        destination = Destination.objects.create(
            name="برج میلاد",
            city="تهران",
            description="نماد تهران",
            price=0
        )

        plan = Plan.objects.create(
            title="سفر تهران",
            description="برنامه تست",
            user=user
        )
        plan.destinations.add(destination)

    def test_all_plans(self):
        query = """
        query {
          allPlans {
            title
            user {
              username
            }
            destinations {
              name
            }
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
        self.assertEqual(len(content["data"]["allPlans"]), 1)
        self.assertEqual(content["data"]["allPlans"][0]["title"], "سفر تهران")
