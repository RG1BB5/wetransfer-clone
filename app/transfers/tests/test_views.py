from django.test import override_settings, tag
from sponge_file_transfer.tests.test_functional.test_user_experience import BaseTestCase

from transfers.models import Transfer

# @override_settings(ALLOWED_HOSTS=['*'])  # Disable ALLOW_HOSTS
# class TestTransferUserExperience(BaseTestCase):
    
#     @tag('selenium')
#     def test_transfer_can_download_multiple_files_as_zip(self):
#         transfer = Transfer()
#         self.chrome.get(f'http://web:8000/transfer/{transfer.uuid}/')
#         self.assertEqual('The install worked successfully! Congratulations!', self.chrome.title)

#     @tag('selenium')
#     def test_can_upload_multiple_files_for_transfer(self):
#         transfer = Transfer()

#     @tag('selenium')
#     def test_transfer_can_require_auth_before_download(self):
#         transfer = Transfer()

#     @tag('selenium')
#     def test_transfer_can_expire(self):
#         transfer = Transfer()