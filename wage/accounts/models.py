from django.db import models
from django.contrib.auth.models import AbstractUser
from rolepermissions.checkers import has_permission, available_perm_names
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission
from django.utils.translation import gettext_lazy as _

############## PYTHON GENERAL IMPORT #############

##############  APP SPECIFIC IMPORT  #############

class User(AbstractUser):
    mobile = models.CharField(max_length=16, null=True, blank=True)
    site_id = models.CharField(max_length=3, default='1')
    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.get_full_name()