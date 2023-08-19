from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:homepage')
