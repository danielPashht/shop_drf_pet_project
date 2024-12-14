import factory.fuzzy
from .models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker(provider='word')
    slug = factory.Faker(provider='slug')
