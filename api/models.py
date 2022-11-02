from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class Miner(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True)
    facility = models.CharField(max_length=32, default="", unique=False)
    machineName = models.CharField(max_length=32, default="", unique=False)
    quantity = models.IntegerField(null=False, default=1)
    power = models.IntegerField(null=False, default=1)
    monthlyFee = models.IntegerField(null=False,default=1)
    miningPool = models.CharField(max_length=32, default="", unique=False)
    status = models.CharField(max_length=32,default="", unique=False)


class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user