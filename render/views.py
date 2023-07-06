from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# df = pd.read_excel('nuevo.xlsx', engine=openpyxl)


def index(request):
    return render(request, "render/index.html", {})


@csrf_exempt
def post_request(request):
    print("post_request INTRO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@qq")
    if request.method == 'POST':
        # procesar los datos recibidos
        # print(request.POST)
        textarea1 = request.POST.get('ntextarea1')
        textarea2 = request.POST.get('ntextarea2')
        t1 = textarea1.split("\r\n")
        t2 = textarea2.split("\r\n")
        t2.extend([None] * (len(t1) - len(t2)))
        # print(t1)
        # print(t2)
        # df = pd.read_excel('nuevo.xlsx')
        data = {
            'A': t1,
            'B': t2
        }
        # print(data)
        df = pd.DataFrame(data)
        # print(df.to_markdown())
        not_in_b = ~df['A'].isin(df['B'])
        result = df['A'][not_in_b]
        print(result.to_markdown())
        rr = result.to_json()
        response_data = {'result': rr}
        return JsonResponse(response_data,
                            status=status.HTTP_200_OK)
    else:
        return JsonResponse({'result': 'error'})
