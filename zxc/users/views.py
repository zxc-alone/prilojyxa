from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('rereww:index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        print("=== form_valid called ===")
        user = form.save()
        print(f"User saved: {user.username}")
        login(self.request, user)
        print("User logged in")
        return redirect(self.success_url)

    def form_invalid(self, form):
        print("=== form_invalid called ===")
        print("Form errors:", form.errors)
        return super().form_invalid(form)