from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from mysite.views import OwnerOnlyMixin
from photo.forms import PhotoInlineFormSet


class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo


#-- Create/Change-List/Update/Delete for Photo
class PhotoCV(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)

class PhotoUV(OwnerOnlyMixin, UpdateView):
    model = Photo
    fields = ('album', 'title', 'image', 'description')
    success_url = reverse_lazy('photo:index')

class PhotoDelV(OwnerOnlyMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


#-- Create/Change-List/Update/Delete for Album
class AlbumChangeLV(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner = self.request.user)

class AlbumDelV(OwnerOnlyMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')


#-- (InlineFormSet) create/update for Album
class AlbumPhotoCV(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    # 장고에서 제공하는 디폴트 컨텍스트 변수 이외에 추가적인 컨텍스트 변수를 정의하기 위해 get_context_data() 메소드를 오버라이딩한다.
    # 여기서는 formset 컨텍스트 변수를 추가한다.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['fomset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['fomset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['fomset']
        
        # 폼셋에 들어있는 각 폼의 owner필드에 현재 로그인된 사용자의 User객체를 할당. 
        # 즉 폼셋에 들어있는 각 사진 폼의 owner 필드를 자동으로 지정
        for photoform in formset:
            photoform.instance.owner = self.request.user

        if formset.is_valid():
            self.object = form.save() # form.save()를 호출에 폼의 데이터를 테이블에 저장. 즉 앨범 레코드를 하나 생성
            formset.instance = self.object # 폼셋의 메인 객체를 방금 테이블에 저장한 객체로 지정
            formset.save() # 앨범 레코드에 1:N관계로 연결된 여러 개의 사진 레코드를 테이블에 저장
            return redirect(self.get_success_url()) # redirect()함수로 페이지를 이동. 앨범 리스트 페이지로 리다이렉트
        else:
            # 폼셋의 데이터가 유효하지 않으면, 다시 메인 폼 및 인라인 폼셋을 출력. 
            return self.render_to_response(self.get_context_data(form=form))

class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
    model = Album
    fields = ('name', 'description')
    success_url = reverse_lazy('photo:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = PhotoInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

        
