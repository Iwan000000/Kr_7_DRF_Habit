from rest_framework import serializers
from habits.models import Habit
from habits.validators import check_duration_time, check_habit_periodicity, validate_fields


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычек"""
    duration_time = serializers.DurationField()
    periodicity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        if data.get('reward'):
            reward = data.get('reward')
        else:
            reward = None
        if data.get('associated_nice_habit'):
            associated_nice_habit = data.get('associated_nice_habit')
        else:
            associated_nice_habit = None
        validate_fields(reward, associated_nice_habit)
        return data


class PublicHabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для общественных привычек"""

    class Meta:
        model = Habit
        fields = ["action", "place", "time", "reward", "associated_nice_habit", "periodicity",
                  "duration_time", "is_public"]
