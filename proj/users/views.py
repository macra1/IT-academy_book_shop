from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from . import forms, models
# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()


def http(request, some_txt):
    return HttpResponse(f"some test http and {some_txt}")


def t3(request):
    return render(request, "ТЗ на создание сайта.htm")


class RegisterView(FormView):
    template_name = "registration/create-user.html"
    form_class = forms.RegisterForm
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        tel = form.cleaned_data.get("tel")
        user = User.objects.create_user(username=username,
                                        password=password)
        profile = models.Profile.objects.create(user=user, tel=tel)
        return super().form_valid(form)
