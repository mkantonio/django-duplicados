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
    if request.method == "POST":
        # print(request.POST)
        textarea1 = request.POST.get("ntextarea1")
        textarea2 = request.POST.get("ntextarea2")
        t1 = textarea1.split("\r\n")
        t2 = textarea2.split("\r\n")
        t2.extend([None] * (len(t1) - len(t2)))
        # df = pd.read_excel('nuevo.xlsx')
        data = {"A": t1, "B": t2}
        # print(data)
        df = pd.DataFrame(data)
        # print(df.to_markdown())

        not_in_b = a_not_in_b_f(df)
        not_in_a = b_not_in_a_f(df)
        duplicados = duplicados_a(df)

        response_data = {
            "result": not_in_b,
            "result2": not_in_a,
            "duplicados": duplicados,
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"result": "error"})


def a_not_in_b_f(df):
    not_in_b = ~df["A"].isin(df["B"])
    result = df["A"][not_in_b]
    print(result.to_markdown())
    return result.to_json()


def b_not_in_a_f(df):
    not_in_b = ~df["B"].isin(df["A"])
    result = df["B"][not_in_b]
    print(result.to_markdown())
    return result.to_json()


def duplicados_a(df):
    duplicates = df[df.duplicated(subset=["A"], keep=False)]["A"]
    counts = duplicates.value_counts().reset_index()
    counts.columns = ["duplicado", "cantidad"]
    counts = counts.sort_values(by="cantidad", ascending=False)
    print(counts.to_markdown())
    return counts.to_json()
