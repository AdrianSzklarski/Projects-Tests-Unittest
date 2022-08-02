import unittest
from e_mail.article.article_email import Email


class TestEmail(unittest.TestCase):

    def setUp(self):
        print('Setting Up...')
        self.email = Email(10, 25, 'jan', 'polak')

    def tearDown(self):
        print('Tearing down...')
        del self.email

    def test_email(self):
        self.assertEqual(self.email.get_contact_author_name, 'Jan.Polak@gmail.com')

    def test_surname(self):
        # Name of a person who does not work for the company
        self.email.surname = 'Kowalski'
        self.assertEqual(self.email.get_contact_author_name, 'Jan.Kowalski@gmail.com')
