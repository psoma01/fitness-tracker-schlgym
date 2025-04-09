from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data_content import test_data
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = {}
        for user_data in test_data['users']:
            user = User.objects.create(
                _id=user_data['_id'],
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            users[user_data['username']] = user

        # Populate teams
        for team_data in test_data['teams']:
            team = Team.objects.create(
                _id=team_data['_id'],
                name=team_data['name']
            )
            team.members = list(users.values())
            team.save()

        # Populate activities
        for activity_data in test_data['activities']:
            Activity.objects.create(
                _id=activity_data['_id'],
                user=users[activity_data['user']],
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration']
            )

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            Leaderboard.objects.create(
                _id=leaderboard_data['_id'],
                user=users[leaderboard_data['user']],
                score=leaderboard_data['score']
            )

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(
                _id=workout_data['_id'],
                name=workout_data['name'],
                description=workout_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
