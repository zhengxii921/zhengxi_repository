from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from ..models import *

class IndexTests(TestCase):


    def test_get(self):
        response = self.client.get(reverse("numazutourist:index"))
        self.assertEqual(response.status_code, 200)


class ReviewsTests(TestCase):


    def setUp(self):
        placetest = Place(
            name="name",
            adress="Tokyo",
            explain="here",
            sort=1,
            opentime="00:00:00",
            closetime="23:59:59",
        )
        placetest.save()

        review = Review.objects.create(
            name = "testuser1",
            text = "text1",
            date = "2020-1-1",
            eva = False,
            place = placetest,
        )


    def test_get(self):
        response = self.client.get(reverse("numazutourist:reviews"))
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        placetest = Place(
            name="name",
            adress="Tokyo",
            explain="here",
            sort=1,
            opentime="00:00:00",
            closetime="23:59:59",
        )
        placetest.save()

        review = Review.objects.create(
            name = "testuser1",
            text = "text1",
            date = "2020-1-1",
            eva = False,
            place = placetest,
        )