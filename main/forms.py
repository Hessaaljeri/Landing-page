from django import forms 



class EmailForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField()
	message = forms.CharField()