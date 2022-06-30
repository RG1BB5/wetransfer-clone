from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from .models import Transfer
from .forms import TransferForm


class HomeView(CreateView):
    model = Transfer
    form_class = TransferForm
    # fields = ['email', 'password', 'expiry_date']

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print('FORM IS_VALID', form.is_valid, form.errors, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        print('FORM_VALID', self.object)
        return super().form_valid(form)


class TransferView(DetailView):
    model = Transfer
    slug_url_kwarg = "uuid"
    slug_field = "uuid"