from django.contrib.auth import login,authenticate,get_user_model , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm, UserDetailEdit


# Create your views here.
def login_user(request):
    login_form= LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if login_form.is_valid():
        user_name=login_form.cleaned_data.get("user_name")
        print(user_name)
        password=login_form.cleaned_data.get("password")
        print(password)
        user=authenticate(request,username=user_name,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'نام کاربری یا کلمه عبور نادرست می باشد ')
    context={
        "login_data": login_form

    }
    return render(request,'account/login.html',context)



def register(request):
    registerform=RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if registerform.is_valid():
        username=registerform.cleaned_data.get('user_name')
        password=registerform.cleaned_data.get('password')
        email=registerform.cleaned_data.get('email')
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('/login')
    context={
        'register_form':registerform
    }
    return render(request,'account/register.html',context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


@login_required(login_url='/login')
def user_edit_account(request):
    user_id = request.user.id
    user: User= User.objects.get(id=user_id) # daghighan hmin ro barmigardone
    # print(user)
    # user_f = User.objects.filter(id=user_id).first() #queryset barmigardone
    # print(user_f)
    if user is None:
        raise Http404('کاربری مورد نظر یافت نشد')
    user_edit_form = UserDetailEdit(request.POST or None,
                               initial={'first_name':request.user.first_name,'last_name':request.user.last_name})
    if user_edit_form.is_valid():
        first_name_form = user_edit_form.cleaned_data.get('first_name')
        last_name_form = user_edit_form.cleaned_data.get('last_name')
        user.first_name = first_name_form
        user.last_name = last_name_form
        user.save()

    context={
        'edit_form': user_edit_form,

    }
    return render(request, 'account/edit_account.html', context)


@login_required(login_url='/login')
def user_slider(request):
    context={

    }
    return render(request, 'account/user_slider.html', context)