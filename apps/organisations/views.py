from django.views.generic import CreateView, ListView, DetailView
from django.core.urlresolvers import reverse

from .forms import OrganisationForm
from .models import Organisation


class OrganisationList(ListView):
    model = Organisation
    paginate_by = 20

    #   We're also going to jam the for on the list view page.
    def get_context_data(self, **kwargs):
        context = super(OrganisationList, self).get_context_data(**kwargs)
        context['total_organisations_in_db'] = Organisation.objects.count()
        return context


class OrganisationCreate(CreateView):
    model = Organisation
    form_class = OrganisationForm

    def get_success_url(self):
        return reverse('organisation-list')


class OrganisationDetail(DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetail, self).get_context_data(**kwargs)
        return context
