from django.views import generic

from .models import Person


class IndexView(generic.DetailView):
    model = Person
    template_name = 'testapps/index.html'

    def get_object(self, queryset=None):
        """Return the last five published questions."""
        return Person.objects.get(pk=1)
