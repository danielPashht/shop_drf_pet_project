import factory.fuzzy
from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    # TODO: Not used yet.
    class Meta:
        model = User

    role = factory.fuzzy.FuzzyChoice(User.Role)
    username = factory.Faker('email')
    password = factory.Faker('password', length=8)


class CustomerFactory(UserFactory):
    role = User.Role.CUSTOMER


class ManagerFactory(UserFactory):
    role = User.Role.MANAGER


class AdminFactory(UserFactory):
    role = User.Role.ADMIN
