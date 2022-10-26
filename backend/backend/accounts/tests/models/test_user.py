from django.contrib.auth import get_user_model
from django.test import TestCase


class UserCreationTest(TestCase):
    def setUp(self):
        """Initialise user instance."""
        User = get_user_model()
        self.user = User.objects.create(username="user1")

    def test_user_has_str(self):
        """Test that user has a defined __str__ method."""
        self.assertEqual(self.user.__str__(), "user1")
