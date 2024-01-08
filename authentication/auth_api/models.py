from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


# Custom User Manager
class HumanManager(BaseUserManager):
    def create_user(self, email, name, tnc, password=None, password2=None):
        if not email:
            raise ValueError("Humans must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tnc=tnc
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tnc, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            tnc=tnc
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




# Custom User Model 
class Human(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20)
    tnc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = HumanManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "tnc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin