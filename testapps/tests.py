from django.test import TestCase
from django.contrib.auth.models import User
from .models import Person


class My42cctestTests(TestCase):
    fixtures = ['person.json', 'users.json']

    def test_homepage(self):
        """
        Test Homepage
        :return:
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        """
        Test admin account
        :return:
        """
        admin_user = User.objects.get(username='admin')
        self.assertEqual(admin_user.email, 'hamza@khchine5.me.uk')

    def test_personal_data(self):
        """
        Test the personal data
        :return:
        """
        hamza_user = Person.objects.get(name='Hamza')
        self.assertEqual(hamza_user.jabber_id, 'khchine05@42cc.co')
        self.assertEqual(hamza_user.email, 'hamza@khchine5.me.uk')
