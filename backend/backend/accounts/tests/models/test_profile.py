from django.contrib.auth import get_user_model
from django.test import TestCase

from ...models import Profile


class ProfileCreationTest(TestCase):
    def setUp(self):
        """Initialise user instance, which creates a profile instance."""
        User = get_user_model()
        self.user = User.objects.create(username="user1")
        self.profile = self.user.profile

    def test_profile_has_str(self):
        """Test that profile has a defined __str__ method."""
        self.assertEqual(self.profile.__str__(), "user1")
