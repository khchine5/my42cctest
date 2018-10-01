from django.views import generic

from .models import Person


class IndexView(generic.DetailView):
    model = Person
    template_name = 'testapps/index.html'

    def get_object(self, queryset=None):
        """Return my personal data."""
        return Person.objects.get(pk=1)
