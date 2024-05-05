from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Создать суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('SUPER_USER'),
            name='admin',
            telegram_chat_id='12345',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password(os.getenv('SUPER_USER_PASS'))
        user.save()
