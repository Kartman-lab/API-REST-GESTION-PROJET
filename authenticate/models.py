from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # tes champs supplémentaires ici
    age = models.PositiveBigIntegerField(default=0)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def has_valid_consent(self):
        return self.age >= 15 and self.can_data_be_shared

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
