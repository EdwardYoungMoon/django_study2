from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

class PostLV(ListView):
    model = Post # PostLV 클래스의 대상 테이블은 Post 테이블이다.
    template_name = 'blog/post_all.html' # 템플릿 파일 지정. 지정하지 않으면 파일명은 'blog/post_list.html'이 된다.
    context_object_name = 'posts' # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정. 
    paginate_by = 2 # 한 페이지에 보여주는 객체 리스트의 숫자. 페이징 기능이 활성화되면 하단에 페이지 이동 버튼을 만들 수 있다.

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'


'''페이징 기능이나 날짜 기반 제네릭 뷰를 직접 코딩한다면 쉽지 않을 것이다. 제네릭 뷰를 통해 복잡한 로직을 장고에서 처리하고,
개발자는 단 몇줄로 코딩을 완료할 수 있다.'''