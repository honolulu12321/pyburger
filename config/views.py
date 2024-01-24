#-*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    # return HttpResponse("안녕하세요, pyburger입니다")  #
    return render(request, "main.html")

def main(request):
    # return HttpResponse("안녕하세요, pyburger입니다")  #
    return render(request, "burger_list.html")


def burger_list(request):
    return HttpResponse("Pyburger의 햄버거 목록입니다")