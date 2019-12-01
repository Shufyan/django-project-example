from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from AppTwo.models import Users
from AppTwo.forms import SignupForm, UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    index_dict = {'text':'hello world', 'number':100}
    return render(request,'apptwo/index.html',context = index_dict)

def help(request):
    help_dict = {'help_text':'Hello, how may I help you?','text':'hello world', 'number':100}
    return render(request,'apptwo/help.html',context = help_dict)

@login_required
def users(request):
    user_list = Users.objects.order_by('first_name')
    user_dict = {'user_records':user_list}
    return render(request,'apptwo/users.html',context = user_dict)

def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'apptwo/signup.html',{'form':form})    

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'AppTwo/registration.html',{'registered':registered,
                                                      'user_form':user_form, 
                                                      'profile_form':profile_form})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    
    else:
        return render(request,'AppTwo/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))







        

