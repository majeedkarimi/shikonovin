from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام و نام خانوادگی خود را وارد نمایید', 'class':'form-control'}),
        label='نام و نام خانوادگی ',
        validators=[validators.MaxLengthValidator(150, 'نام و نام خانوادگی نمی تواند بیشتر از 150 کارکتر باشد')]
            )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد نمایید','class':'form-control'}),
        label='ایمیل ',
        validators=[validators.MaxLengthValidator(100, 'ایمیل نمی تواند بیشتر از 100 کارکتر باشد')]

    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا عنوان پیام خود را وارد نمایید','class':'form-control'}),
        label='عنوان ',
        validators=[validators.MaxLengthValidator(200, 'عنوان نمی تواند بیشتر از 200 کارکتر باشد')]
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'لطفا متن پیام خود را وارد کنید','class':'form-control', }),
        label='متن پیام ',
    )