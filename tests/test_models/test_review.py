#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review_place_id(self):

        review1 = Review()
        self.assertTrue(hasattr(review1, "place_id"))
        self.assertEqual(review1.place_id, "")
        review1.place_id = "Excelent"
        self.assertEqual(review1.place_id, "Excelent")

    def test_review_user_id(self):

        review1 = Review()
        self.assertTrue(hasattr(review1, "user_id"))
        self.assertEqual(review1.user_id, "")
        review1.user_id = "051051"
        self.assertEqual(review1.user_id, "051051")

    def test_review_text(self):

        review1 = Review()
        self.assertTrue(hasattr(review1, "text"))
        self.assertEqual(review1.text, "")
        review1.text = "HBNB"
        self.assertEqual(review1.text, "HBNB")
