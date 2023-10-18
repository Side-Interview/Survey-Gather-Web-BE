from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from common.models import CreateAtUpdateAt


class BaseUserManager(BaseUserManager):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(CreateAtUpdateAt, AbstractBaseUser, PermissionsMixin):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    email = models.EmailField(
        verbose_name="email address",
        max_length=128,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    is_agree_privacy = models.BooleanField(default=True)
    is_agree_marketing = models.BooleanField(default=False)

    last_passsword_change_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    nickname = models.CharField(max_length=8)
    thumnail_image_url = models.CharField(max_length=512)
    name = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=16)

    gender = models.CharField(
        max_length=8,
        choices=GenderChoices.choices,
    )
    # MEMO : 반영 여부 모름
    # address = models.CharField(max_length=64)
    # address_detail = models.CharField(max_length=64)
    birth = models.DateField()

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
