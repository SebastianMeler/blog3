from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        author = User.objects.create()
        Post.objects.create(author=author)

    def test_model_post_str(self):
        post = Post(title="test")
        self.assertEqual(post.title, "test")
        self.assertEqual(post.__str__(), "test")
