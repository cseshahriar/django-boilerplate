import logging
from django.core.management.base import BaseCommand
from users.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(email="admin@me.com")
        user.set_password("admin123#")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        logger.info(f"user created {user}")

        self.stdout.write(
            self.style.SUCCESS('Successfully closed')
        )
