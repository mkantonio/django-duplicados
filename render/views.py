from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# df = pd.read_excel('nuevo.xlsx', engine=openpyxl)






def index(request):
    return render(request, "render/index.html", {})


@csrf_exempt
def post_request(request):
    if request.method == 'POST':
        # df = pd.read_excel('nuevo.xlsx')
        # not_in_d = ~df['C'].isin(df['D'])
        # result = df['C'][not_in_d]
        # print(result)
        # procesar los datos recibidos
        body = request.POST.get('body')
        textarea1 = body.field1
        textarea2 = body.field2
        print(textarea1)
        print(textarea2)
        response_data = {'result': 'success'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'result': 'error'})
