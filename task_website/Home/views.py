from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django import template

from .models import University, Profile, Notifications

from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ProfileForm

# Create your views here.
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
# Create your views here.


def Signout(request):
    logout(request)
    return redirect('/login')


def Signup_view(request):
    print(request)
    if request.method == 'POST':
        print(request.FILES)
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            # login()
            login(request, user)
            return redirect('/home')
            # redirect(home_page)
        else:
            print(form.errors)
            return render(request, 'signup.html', {'form': form})

    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'signup.html', {'form': form})

# def Signup_view(request):
#     context = {}
#     context['form'] = SignupForm()


#     return render(request, "signup.html", context)
def Login_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, Username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def home_page(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        colleges = University.objects.all()
        user = request.user
        print(type(colleges))
        context = {
            "colleges": colleges,
            "user": user,
            "bookmarks": user.getBookmarks().get("bookmarks"),
            "applications": user.getApplications().get("applications")
        }

        # return response with template and context
        return render(request, "home.html", context)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def addBookmark(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        # get the form data

        univ = request.POST.get("university", None)
        print(univ)
        if univ is not None:
            bookmarks = request.user.getBookmarks()
            print(bookmarks.get("bookmarks"))
            new_b = bookmarks.get("bookmarks")+[univ]
            print(new_b)
            request.user.setBookmarks({"bookmarks": new_b})
        # save the data and after fetch the object in instance

        return JsonResponse({"data": "success", "userb": request.user.getBookmarks()}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"data": "failed"}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def addApplication(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        # get the form data

        univ = request.POST.get("university", None)
        print(univ, "adding application")
        if univ is not None:
            applications = request.user.getApplications()
            print(applications.get("applications"))
            new_b = applications.get("applications")
            if(univ not in new_b):
                new_b = new_b+[univ]
                print(new_b,"adding")
                request.user.setApplications({"applications": new_b})
        # save the data and after fetch the object in instance

        return JsonResponse({"data": "success", "userA": request.user.getApplications()}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"data": "failed"}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def removeBookmark(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        # get the form data
        univ = request.POST.get("university", None)
        print(univ)
        if univ is not None:
            bookmarks = request.user.getBookmarks()
            print(bookmarks.get("bookmarks"))
            new_b = bookmarks.get("bookmarks")

            if univ in bookmarks.get("bookmarks"):
                new_b.remove(univ)
                if(new_b is None):
                    request.user.setBookmarks({"bookmarks": []})
                else:
                    request.user.setBookmarks({"bookmarks": new_b})
        # save the data and after fetch the object in instance

        return JsonResponse({"data": "success", "userb": request.user.getBookmarks()}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"data": "failed"}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def removeApplication(request):
    # request should be ajax and method should be POST.
    if is_ajax(request=request) and request.method == "POST":
        # get the form data
        univ = request.POST.get("university", None)
        print(univ,"remove")
        if univ is not None:
            applications = request.user.getApplications()
            new_b = applications.get("applications")
            print(new_b,"remove appl")

            if univ in applications.get("applications"):
                new_b.remove(univ)
                if(new_b is None):
                    request.user.setApplications({"applications": []})
                else:
                    request.user.setApplications({"applications": new_b})
        # save the data and after fetch the object in instance

        return JsonResponse({"data": "success", "userA": request.user.getApplications()}, status=200)
    else:
        # some form errors occured.
        return JsonResponse({"data": "failed"}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def Bookmarks_view(request):
    if request.method == 'GET':

        bookmarks = request.user.getBookmarks().get("bookmarks")
        applications = request.user.getApplications().get("applications")

        colleges = University.objects.all().filter(Name__in=bookmarks)

        # colleges = University.objects.all().filter(Name__in=bookmarks)
        print(colleges, " bookmarks")
        context = {
            "colleges": colleges,
            "user": request.user,
            "bookmarks": bookmarks,
            "applications": applications
        }

        # return response with template and context
        return render(request, "bookmarks.html", context)


def Applications_view(request):
    if request.method == 'GET':

        applications = request.user.getApplications().get("applications")

        colleges = University.objects.all().filter(Name__in=applications)

        # colleges = University.objects.all().filter(Name__in=bookmarks)
        print(colleges, " bookmarks")
        context = {
            "colleges": colleges,
            "user": request.user,
            "applications": applications
        }

        # return response with template and context
        return render(request, "applications.html", context)


def Notifications_view(request):
    if request.method == 'GET':

        notifs = Notifications.objects.all().filter(user=request.user)

        # colleges = University.objects.all().filter(Name__in=bookmarks)
        print(notifs, " bookmarks")
        context = {
            "user": request.user,
            "notifications": notifs
        }

        # return response with template and context
        return render(request, "notifications.html", context)


def getUniversityCard(request):
    # request should be ajax and method should be GET.
    if is_ajax(request=request) and request.method == "GET":
        # get the nick name from the client side.
        continent = request.GET.get("Continent", None)
        if(continent == ''):
            data = University.objects.all()
        else:
            data = University.objects.all().filter(Continent=continent)
        # check for the nick name in the database.

        context = {
            "colleges": data,
            "user": request.user,
            "bookmarks": request.user.getBookmarks().get("bookmarks"),
            "applications": request.user.getApplications().get("applications")
        }

        if data.exists():
            # if nick_name found return not valid new friend
            html = render_to_string('collegelist.html', context)
            return HttpResponse(html)
        else:
            return HttpResponse("")

    return JsonResponse({}, status=401)

@login_required(login_url="/login")
def ProfileUpdate(request):
    print(request.user)
    if request.method == 'POST':
       
        form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            user = form.save(request.user.id)
            # login()
            return redirect('/home')
            # redirect(home_page)
        else:
            print(form.errors)
            return render(request, 'profileupdate.html', {'form': form,'user':request.user})

    else:
        form = ProfileForm(instance=request.user,initial={"Username": request.user.Username, "Email": request.user.Email})
        context = {
            'form': form
        }
    return render(request, 'profileupdate.html', {'form': form, 'user': request.user})
