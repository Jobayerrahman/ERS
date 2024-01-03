from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class userManager(BaseUserManager):
    def create_user(self,email,username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user    = self.create_user(
            email=self.normalize_email(email),
            password= password,
            username=username,
        )

        user.is_admin =True
        user.is_staff =True
        user.is_superuser =True
        user.save(using=self._db)
        return user


class userInformation(AbstractBaseUser):
    first_name                          =models.CharField(max_length=30)
    last_name                           =models.CharField(max_length=30)

    username                            =models.CharField(max_length=30, unique=True)
    email                               =models.EmailField(verbose_name="email",max_length=60, unique=True)


    date_joined                         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login                          = models.DateTimeField(verbose_name='last login', auto_now=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username'] 

    objects =userManager()

    def __str__(self):
        return self.email + "," + self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.date_joined is None:
            self.date_joined = timezone.now()
        elif not self.date_joined is not None:
            self.date_joined = None
        super(userInformation, self).save(*args, **kwargs)

