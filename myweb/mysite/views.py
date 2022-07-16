from tempfile import template
from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import AccessMixin # view 처리 진입 단계에서 적절한 권한을 가졌는지 판별

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


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True # 403 error
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs): # maim method인 get() 처리 이전 단계인 dispatch()를 오버라이딩. 
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)