from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser



class AbstractUserCustom(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        ("username"),
        max_length=150,
        default="",
        help_text= (
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    email = models.EmailField(("email address"), blank=True)
    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text= ("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)