from django import forms

class Sessioncountform(forms.Form):
    date = forms.IntegerField(help_text='YYMMDD')