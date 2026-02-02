from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          #you can login after registeration
        #   login(request, form.save())
          return redirect("posts:lists")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request, 'users/register.html',context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            #the logic below fetches next which takes a user the clicked page when not logged in immediately the user logins in
            if 'next' in request.POST:
                return request.POST.get('next')
            return redirect("posts:lists")
    else:
        form = AuthenticationForm()
    context = {"form":form}
    return render(request, 'users/login.html',context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")