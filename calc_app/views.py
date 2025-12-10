from django.shortcuts import render


def calculator(request):

    list=[0,1,2,3,4,5,6,7,8,9]
    expression = ""

    if request.method == "POST":
        old = request.POST.get("expression", "")
        btn = request.POST.get("btn")

        if btn == "=":
            try:
                expression = str(eval(old))
            except Exception as a:
                expression = a

        elif btn == "C":
            expression = ""

        else:
            expression = old + btn

    return render(request, "index.html", {"result": expression,'list':list})

