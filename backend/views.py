import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from backend.judge.Huffman.hftree import encode, decode, cipher_book
from backend.judge.BalancedBinaryTree.balanced_binary_tree import balanced


def index(request):
    return render(request, 'index.html')


# Create your views here.

@csrf_exempt
def balanced_binary_tree(request):
    # 生成 csrf 数据，发送给前端
    return HttpResponse(json.dumps(balanced(request.POST["user_input"])))


@csrf_exempt
def huffman_encode(request):
    # 生成 csrf 数据，发送给前端
    x = csrf(request)
    csrf_token = x['csrf_token']
    """
    获取数据:
    """
    plain_text = request.POST["user_input"]
    """
    加密:
    """
    code = encode(plain_text)
    return HttpResponse(code)


@csrf_exempt
def huffman_decode(request):
    # 简化过程 人生苦短
    return HttpResponse(decode(request.POST["user_input"]))


@csrf_exempt
def cipher_book():
    return HttpResponse(json.dumps(cipher_book))
