from django.db import models


# Create your models here.

class Person(models.Model):
    """
    Person class.
    """

    name = models.CharField(
        'First name', max_length=50)
    surname = models.CharField(
        'Second name', max_length=50)
    date_birth = models.DateField("Date of Birth")
    bio = models.TextField('bio', max_length=1000)
    #Contact
    email = models.EmailField('Email', max_length=255)
    jabber_id = models.CharField('Jabber ID', max_length=255)
    skype_id = models.CharField('Skype ID', max_length=255)
    other_contacts = models.TextField('Others contacts', max_length=255)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
