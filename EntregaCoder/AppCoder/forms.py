from django import forms

class productoFormulario(forms.Form):

    title = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=20, decimal_places=2)
    thumbnail = forms.CharField(max_length=400)

class messageHub(forms.Form):
    user = forms.CharField(max_length=100)
    message = forms.CharField(max_length=300)