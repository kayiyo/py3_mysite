from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import BlogsPost


class TestBlog(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = BlogsPost(pub_date=time)
        self.assertIs(future_question.test_was_published_recently(), False)