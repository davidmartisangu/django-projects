from django.test import TestCase

from profiles.models import UserProfile, Follow
from django.contrib.auth.models import User

class UserProfileModelTest(TestCase):
    def setUp(self):

        # Creamos usuarios y perfiles
        self.user1 = User.objects.create_user(
            username="john",
            email="john@lenon.com",
            password="password123"
        )

        self.user2 = User.objects.create_user(
            username="paul",
            email="paul@mccartney.com",
            password="password123"
        )

        self.profile1 = UserProfile.objects.create(
            user=self.user1,
            bio="I´m a musician",
            birth_date="1940-10-09"
        )

        self.profile2 = UserProfile.objects.create(
            user=self.user2,
            bio="I´m also a musician",
            birth_date="1942-06-18"
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile1.bio, "I´m a musician")
        self.assertEqual(self.user1.username, "john")

    def test_follow_user(self):
        # llama al método para que profile1 siga a profile2
        created = self.profile1.follow(self.profile2)
        # Verificamos que existe una relación en el modelo Follow
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following= self.profile2).exists())
        created = self.profile1.follow(self.profile2)
        self.assertFalse(created)
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following= self.profile2).exists())

    def test_unfollow_user(self):
        # llama al método para que profile1 siga a profile2
        self.profile1.follow(self.profile2)
        # Verificamos que existe una relación en el modelo Follow
        self.assertTrue(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())
        # llama al método para que profile1 deje de seguir a profile2
        self.profile1.unfollow(self.profile2)
        # Verificamos que deja de exister una relación en el modelo Follow
        self.assertFalse(Follow.objects.filter(follower=self.profile1, following=self.profile2).exists())

    def test_str_userprofile(self):
        self.assertEqual(str(self.profile1), self.profile1.user.username)

class FollowModelTest(TestCase):
    def setUp(self):
        # Creamos usuarios y perfiles
        self.user1 = User.objects.create_user(
            username="john",
            email="john@lenon.com",
            password="password123"
        )

        self.user2 = User.objects.create_user(
            username="paul",
            email="paul@mccartney.com",
            password="password123"
        )

        self.profile1 = UserProfile.objects.create(
            user=self.user1,
            bio="I´m a musician",
            birth_date="1940-10-09"
        )

        self.profile2 = UserProfile.objects.create(
            user=self.user2,
            bio="I´m also a musician",
            birth_date="1942-06-18"
        )

    def test_unique_follow_once_time(self):
        Follow.objects.get_or_create(follower=self.profile1, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(),1)
        Follow.objects.get_or_create(follower=self.profile1, following=self.profile2)
        self.assertEqual(Follow.objects.filter(follower=self.profile1, following=self.profile2).count(),1)