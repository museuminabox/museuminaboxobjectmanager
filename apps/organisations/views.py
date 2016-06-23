from django.views.generic import ListView

from .models import Organisation


class OrganisationList(ListView):
    model = Organisation
    paginate_by = 20

    #   We're also going to jam the for on the list view page.
    def get_context_data(self, **kwargs):
        context = super(OrganisationList, self).get_context_data(**kwargs)
        return context
