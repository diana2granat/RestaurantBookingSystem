from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission)
from django.utils import timezone

# Create your models here.
class UserManager (BaseUserManager):
    def create_user (self, email, password, **extra_fields):
        if not email:
            raise ValueError ("Email must be set")
        email = self.normalize_email (email)
        user = self.model (email=email, **extra_fields)
        user.set_password (password)
        user.save ()
        return user
    
    def create_superuser (self, email, password, **extra_fields):
        extra_fields.setdefault ("is_staff", True)
        extra_fields.setdefault ("is_superuser", True)

        if extra_fields.get ("is_staff") is not True:
            raise ValueError ("Superuser must have is_staff = True")
        if extra_fields.get ("is_superuser") is not True:
            raise ValueError ("Superuser must have is_superuser = True")
        return self.create_user (email, password, **extra_fields)

    
class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField (unique=True)
    is_staff = models.BooleanField (default=False)
    is_active = models.BooleanField (default=True)
    date_joined = models.DateTimeField (default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__ (self):
        return self.email

    # Add a related_name argument to avoid clash with auth.User.groups
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # You can choose any meaningful name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Add a related_name argument to avoid clash with auth.User.user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # You can choose any meaningful name
        blank=True,
        help_text='Specific permissions for this user.',
    )
    