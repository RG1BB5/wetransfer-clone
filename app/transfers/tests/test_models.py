import datetime
from django.core.files.base import ContentFile
from django.test import TestCase
from django.utils.timezone import now

from transfers.models import Transfer, TransferFile

class TransferModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.transfer_one = Transfer.objects.create(email='test@rhysgibbs.co.uk')
        content_file = ContentFile(b'Hello world!', name='hello-world.txt')
        file_one = TransferFile.objects.create(file=content_file, transfer=cls.transfer_one)
        
        cls.transfer_two = Transfer.objects.create(email='test@rhysgibbs.co.uk')
        file_two = TransferFile.objects.create(file=content_file, transfer=cls.transfer_two)
        file_three = TransferFile.objects.create(file=content_file, transfer=cls.transfer_two)

    def test_url_is_random_and_unique(self):
        transfer = Transfer.objects.get(id=1)
        self.assertEqual(transfer.get_absolute_url(), f'/transfer/{transfer.uuid}/')

    def test_can_have_multiple_files(self):
        transfer = Transfer.objects.create(email='test@rhysgibbs.co.uk')
        content_file = ContentFile(b'Hello world!', name='hello-world.txt')
        file_one = TransferFile.objects.create(file=content_file, transfer=transfer)
        file_two = TransferFile.objects.create(file=content_file, transfer=transfer)
        self.assertEqual(transfer.files.count(), 2)

    def test_can_require_auth_via_password(self):
        transfer = Transfer.objects.create(email='test@rhysgibbs.co.uk', password='password')
        content_file = ContentFile(b'Hello world!', name='hello-world.txt')
        file_one = TransferFile.objects.create(file=content_file, transfer=transfer)
        self.assertTrue(transfer.requires_auth)

    def test_can_set_expiry(self):
        transfer = Transfer.objects.create(email='test@rhysgibbs.co.uk')
        content_file = ContentFile(b'Hello world!', name='hello-world.txt')
        file_one = TransferFile.objects.create(file=content_file, transfer=transfer)
        self.assertEquals(transfer.expiry_date, now().date() + datetime.timedelta(days=30))