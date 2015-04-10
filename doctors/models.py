from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from core import labels


class Doctor(models.Model):
    """
    This model stores the "doctors" in the sense that clients make appointments to see doctors, typically
    """
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)
    first_name = models.CharField(_('First name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last name'), max_length=255, blank=True)
    email = models.EmailField(_('Email address'), blank=True)
    phone = PhoneNumberField(_('Phone Number'), max_length=255, blank=True)
    creator = models.ForeignKey(User, verbose_name=_("Creator"), on_delete=models.PROTECT)
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this doctor should be treated as '
                                                'active.'))

    class Meta:
        verbose_name = getattr(labels, 'DOCTOR', _("Doctor"))
        verbose_name_plural = getattr(labels, 'DOCTOR', _("Doctors"))

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()