# -*- encoding: utf-8 -*-
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse


#### USER MODELS AND MANAGERS
class User(AbstractBaseUser):
    """ The User model with custom fields with referral logic where the referral code is the username
    inheritting :class:``AbstractBaseUser``.
    Set ``AUTH_USER_MODEL`` in settings to be able to use it.

     Example:
         
          ### SETTINGS.PY
        ``AUTH_USER_MODEL = 'accounts.User'``
    """
    username = models.CharField(_('username'), unique=True, max_length=12, default=None)
    email = models.EmailField(_('email address'), unique=True, max_length=64)
    first_name = models.CharField(_('first name'), max_length=16)
    last_name = models.CharField(_('last name'), max_length=16)
    main_balance = models.IntegerField(default=0, null=False)
    referral_balance = models.IntegerField(default=0, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    def get_user_permissions(self, obj=None):
        """
        Return a list of permission strings that this user has directly.
        Query all available auth backends. If an object is passed in,
        return only permissions matching this object.
        """
        return UserManager._user_get_permissions(self, obj, 'user')

    def get_group_permissions(self, obj=None):
        """
        Return a list of permission strings that this user has through their
        groups. Query all available auth backends. If an object is passed in,
        return only permissions matching this object.
        """
        return UserManager._user_get_permissions(self, obj, 'group')

    def get_all_permissions(self, obj=None):
        return UserManager._user_get_permissions(self, obj, 'all')

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return UserManager._user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Return True if the user has each of the specified permissions. If
        object is passed, check if the user has all required perms for it.
        """
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use similar logic as has_perm(), above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return UserManager._user_has_module_perms(self, app_label)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'

    @property
    def referral_code(self):
        return self.username
    
    @property
    def referral_link(self):
        return reverse('register') + '?ref=' + self.referral_code
    
    @staticmethod
    def get_user_by_referral_code(referral_code):
        try:
            user = User.objects.get(username=referral_code)
            return user
        except User.DoesNotExist:
            return None


### REFERRALS
class referral_program(models.Model):
    PENDING = 'Pending'
    SUCCESSFUL = 'Successful'
    REFERRAL_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (SUCCESSFUL, 'Successful'),
    )
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('User', blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=13, choices=REFERRAL_STATUS_CHOICES, default=PENDING)
    referrals = models.ForeignKey('User', blank=True, on_delete=models.CASCADE, related_name='referral_field', default=None)
    award_bonus = models.IntegerField(blank=True, default=5)

    def __str__(self):
        return f'({self.status}) {self.user.username} {self.date}'










