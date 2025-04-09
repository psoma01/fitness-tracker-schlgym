from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="00:30:00")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Workout A", description="Test workout")
        self.assertEqual(workout.name, "Workout A")