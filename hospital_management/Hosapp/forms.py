from django import forms
from Hosapp.models import patientmodel,doctormodel

class patientForm(forms.ModelForm):
    class Meta:
        model=patientmodel
        fields="__all__"
        widgets={
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'dob':forms.DateInput(attrs={'class':'form-control'}),
                    'gender':forms.Select(attrs={'class':'form-control'}),
                    'address':forms.TextInput(attrs={'class':'form-control'}),
                    'contact_number':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class doctorForm(forms.ModelForm):
    class Meta:
        model = doctormodel
        fields = '__all__'
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'speciality':forms.TextInput(attrs={'class':'form-control'}),
                    'contact_number':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
        }