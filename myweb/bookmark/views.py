import bookmark
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # @login_required() 데코레이터 기능을 클래스에 적용할 때 사용. 사용자가 로그인된 경우는 정상 처리를 하지만, 로그인 안 된 사용자라면 로그인 페이지로 리다이렉트
from django.urls import reverse_lazy #
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark



class BookmarkCreateView(LoginRequiredMixin ,CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form): # 폼에 입력된 내용에 대해 유효성 검사를 수행해 에러가 없는 경우 form_valid() 호출.
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')


