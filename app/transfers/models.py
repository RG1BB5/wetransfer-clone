import datetime
from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

from base.models import BaseModel


class Transfer(BaseModel):
    class Meta:
        verbose_name = _('Transfer')
        verbose_name_plural = _('Transfers')

    email = models.EmailField(
        help_text=_('Enter your email so that we have a way of notifying you.')
    )

    uuid = models.UUIDField(
        default=uuid4,
        unique=True
    )

    password = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_('If you would like to password protect the files please enter a password.')
    )

    expiry_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('If you would like the files to expire by a certain date, note that if no date is entered files will automatically be removed within 30 days.')
    )

    def get_absolute_url(self):
        return reverse('transfer', kwargs={'uuid': self.uuid})

    @property
    def requires_auth(self):
        return self.password is not None

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = now().date() + datetime.timedelta(days=30)
        super().save(*args, **kwargs)

    
class TransferFile(BaseModel):
    class Meta:
        verbose_name = _('Transfer File')
        verbose_name_plural = _('Transfer Files')

    transfer = models.ForeignKey(
        'transfers.Transfer',
        on_delete=models.CASCADE,
        related_name='files'
    )

    file = models.FileField()