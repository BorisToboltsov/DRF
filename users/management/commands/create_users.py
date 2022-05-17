from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Создание случайных пользователей"

    def add_arguments(self, parser):
        parser.add_argument("total", type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        count = options["total"]
        print("Create superuser.\nLogin: admin\nPassword: admin ")
        User.objects.create_superuser(
            username="admin", first_name="admin", last_name="admin", email="admin@admin.admin", password="admin"
        )
        print("Done")
        for i in range(count):
            user = User.objects.create_user(
                username=f"nname{i}", first_name=f"fname{i}", last_name=f"lname{i}", email=f"email{i}@email.email"
            )
            print(f"user {user} created")
        print("Done")
