from django import forms
from django.contrib.auth.models import User
from django.core import validators


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید:'}),
        label="نام کاربری:"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور خود را وارد کنید:'}),
        label="کلمه عبور:"
    )
    # def clean_user_name(self):
    #     username=self.cleaned_data.get('user_name')
    #     is_exist_user=User.objects.filter(username=username).exists()
    #     if not is_exist_user:
    #         raise forms.ValidationError("کاربری با این مشخصصات یافت نشد")
    #     return username


class RegisterForm(forms.Form):
    user_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید '}),
        label='نام کاربری: ',
        validators=[
            validators.MaxLengthValidator(20,'تعداد کاراکتر نام کاربری نباید بیشتر از 20 عدد باشد'),
            validators.MinLengthValidator(5,'تعداد کاراکتر نام کاربری نباید کمتر از 5 عدد باشد'),
        ]
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد کنید'}),
        label='ایمیل: '
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا کلمه عبور خود را وارد کنید'}),
        label='کلمه عبور: '
    )
    re_password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا تکرار کلمه عبور خود را وارد کنید'}),
        label='تکرار کلمه عبور: '
    )

    def clean_re_password(self):
        password=self.cleaned_data.get('password')
        re_password=self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه عبور و تکرار کلمه عبور یکسان نمی باشد ')
        return password

    def clean_user_name(self):
        username=self.cleaned_data.get('user_name')
        user_exist=User.objects.filter(username=username).exists()
        if user_exist:
            raise forms.ValidationError('این نام کاربری قبلا ثبت شده است !!!')
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_exist=User.objects.filter(email=email)
        if email_exist:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است !!!')
        return email


class UserDetailEdit(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام ',
        validators=[validators.MaxLengthValidator(100, 'نام  نمی تواند بیشتر از 100 کارکتر باشد')]
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی ',
        validators=[validators.MaxLengthValidator(100, 'نام خانوادگی نمی تواند بیشتر از 100 کارکتر باشد')]
    )
