from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")


def results(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'loc': request.POST['location'],
            'lang': request.POST['language'],
            'com': request.POST['comment'],
        
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')














# def results(request):
#     return render(request, "results.html")

# def some_function(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	val_from_field_two = request.POST["two"]

# def some_function(request):
#     if request.method == "GET":
#         print("a GET request is being made to this route")
#         return render(request,"#")
#     if request.method == "POST":
#         print("a POST request is being made to this route")
#         return redirect("/")
    
    
# def some_function(request):
#     if request.method == "GET":
#     	print(request.GET)
#     if request.method == "POST":
#         print(request.POST)
    