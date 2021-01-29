from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import random

meta_data = json.loads(open('data.json', 'r').read())

def img_switch(request):
    type_img = open('img_type.txt', 'r').read()

    if type_img == 'a':
        type_img = 'b'
    elif type_img == 'b':
        type_img = 'a'
    with open('img_type.txt', 'w') as f:
        f.write(type_img)

    return HttpResponse()

def index(request):
    return render(request, 'index.html')

def data(request):
    meta = ['temperature', 'pressure', 'humidity']
    stats_len = 4
    res = {}
    for k in meta_data:
        res[k] = {}
    for i in meta:
        for j in range(1, stats_len + 1):
            key = 'stat' + str(j)
            res[key][i] = meta_data[key][i][random.randint(0, 399)]
    return JsonResponse(res)

def wafer_detail(request):
    type_img = open('img_type.txt', 'r').read()
    return render(request, 'wafer_detail.html', {'path': '/static/img/' + type_img + '/train_00000.png', 'id': request.GET.get('id')})
