from django.forms import inlineformset_factory # 인라인 폼셋을 반환하는 함수 임포트
from photo.models import Album, Photo

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
        fields = ['image', 'title', 'description'], 
        extra = 2) # formset에 들어 있는 빈 폼의 개수는 두개로 지정한다.

"""
formset이란 form 여러 개로 구성된 form을 말한다. 인라인 폼셋이란 메인 폼에 딸려 있는 하위 폼셋을 말하는 것으로,
테이블 간의 관계가 1:N인 경우, N 테이블의 레코드 여러 개를 한꺼번에 입력받기 위한 폼으로 사용된다.
"""