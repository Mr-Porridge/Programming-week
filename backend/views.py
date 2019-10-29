import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from backend.judge.Huffman.hftree import encode, decode, show_cipher_book
from backend.judge.BalancedBinaryTree.balanced_binary_tree import balanced
from backend.message_board.message_operation import mes_to_sql, mes_load


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
    # x = csrf(request)
    # csrf_token = x['csrf_token']
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
    result = decode(request.POST["user_input"])
    return HttpResponse(result)


@csrf_exempt
def cipher(request):
    return HttpResponse(json.dumps(show_cipher_book(request.POST["user_input"])))


@csrf_exempt
def message_save(request):
    print(request.POST["user_input"], request.POST["friend_name"], request.POST["encoded_text"])
    mes_to_sql(request.POST["friend_name"], request.POST["user_input"], request.POST["encoded_text"])
    return HttpResponse("HELLO")


@csrf_exempt
def message_load(request):
    return HttpResponse(json.dumps(mes_load()))
