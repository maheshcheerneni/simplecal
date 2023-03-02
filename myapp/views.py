from django.shortcuts import render
# Create your views here.


def calculter(request):
    total_Amount = 0
    interest = 0
    p=0
    try:
        if request.method == "POST":
            p = eval(request.POST.get("Principul"))
            r = eval(request.POST.get("rate"))
            t = eval(request.POST.get("time"))
            interest = (p*t*r)/100
            rate = interest/(p*t)
            time = interest/(p*r)
            total_Amount =total_Amount+ interest+p
    except:
        print("invalid input ....")
    return render(request,'cal.html',{"total":total_Amount,"inter":interest,"p":p})
