from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone #models의 pub_date값은 자동으로 입력받을 예정이니까 timezone을 불러온다
from .models import Blog
from .forms import NewBlog
#맨처음 페이지
def welcome(request):
    return render(request,'viewcrud/index.html')

#조회 함수
def read(request):
    blogs = Blog.objects.all() #model의 모든 객체를 가져오고 싶음 왜냐? 조회하고 싶으니까
    return render(request, 'viewcrud/funccrud.html',{'blogs':blogs})
#글쓰기 함수
def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    
    # 글쓰기 페이지를 띄워주는 역할 == GET
    return

#수정 함수
def update(request, pk):

    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
     

    #해당하는 블로그 객체 pk에 맞는 입력공간
    return

#삭제함수
def delete(request, pk):
    return

def add_comment(request, pk):
    return