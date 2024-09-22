from django import forms


class GenerateForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=8, help_text="请在name参数输入花名")
    angle = forms.FloatField(min_value=-180, max_value=180, initial=5.0)
    download = forms.BooleanField(initial=False)
