from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET']) #HelloAPI라는 함수가 GET 요청을 받을 수 있는 API라는 것을 @api_view 라는 표기법으로 나타낸다고 생각
def HelloAPI(request):
    return Response("hello wordl!")