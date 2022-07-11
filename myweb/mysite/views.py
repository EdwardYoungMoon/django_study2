from tempfile import template
from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#-- Homepage view
class HomeView(TemplateView):
    template_name = 'home.html'

#-- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done') #form에 입력된 내용에 에러가 없고 table record 생성이 완료된 후 이동할 url지정


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'