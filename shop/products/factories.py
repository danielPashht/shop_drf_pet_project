import factory.fuzzy
from .models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    discount_choices = [(i, i) for i in range(5, 100, 5)]
    discount = factory.fuzzy.FuzzyChoice(discount_choices)
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    price = factory.fuzzy.FuzzyDecimal(1.0, 100.0)
    image = factory.django.ImageField(color='blue')
    category = factory.SubFactory('category.factories.CategoryFactory')

