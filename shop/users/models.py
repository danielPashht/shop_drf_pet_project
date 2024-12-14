from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    REQUIRED_FIELDS = ['password', 'email']
    cart = models.OneToOneField(
        "carts.Cart",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_cart"
    )

    def __str__(self):
        return "{}".format(self.email)

    class Role(models.TextChoices):
        ADMIN = 'admin', _('Admin')
        MANAGER = 'manager', _('Manager')
        CUSTOMER = 'customer', _('Customer')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        default='customer',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        related_query_name='user',
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = self.Role.MANAGER
        super().save(*args, **kwargs)

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER

    @property
    def is_customer(self):
        return self.role == self.Role.CUSTOMER

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN
