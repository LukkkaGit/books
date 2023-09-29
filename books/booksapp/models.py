# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# # Create your models here.
# # class CustomUser(AbstractUser):
# #     STATUS = (
# #         ('regular','regular'),
# #         ('subscriber','subscriber'),
# #         ('moderator','moderator'),
# #     )
# #     email = models.EmailField(unique=True)
# #     status = models.CharField(max_length=100, choices=STATUS, default='regular')
# #     description = models.TextField('Description', max_length=600, default='', blank=True)
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
    

#     def create_superuser(self, email, password=None, **extra_fields):
#         # Your superuser creation logic here


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Define a custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Define the custom user model
class CustomBookUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Add any additional fields you need for your user model here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
