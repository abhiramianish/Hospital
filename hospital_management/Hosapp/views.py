from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from Hosapp.forms import patientForm,doctorForm
from Hosapp.models import patientmodel,doctormodel
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class patientregister(CreateView):
    form_class=patientForm
    template_name='patientregister.html'
    model=patientmodel
    success_url=reverse_lazy('list_view')

class doctorregister(CreateView):
    form_class=doctorForm
    template_name='doctorregister.html'
    model=doctormodel
    success_url=reverse_lazy('doclist_view')

class patientlist(ListView):
    model=patientmodel
    template_name='patientlist.html'
    context_object_name='datakey'

class doctorlist(ListView):
    model=doctormodel
    template_name='doctorlist.html'
    context_object_name='datakey'

class patientedit(UpdateView):
    model=patientmodel
    template_name='patientedit.html'
    success_url=reverse_lazy('list_view')
    pk_url_kwarg='id'
    form_class=patientForm

class patientdelete(DeleteView):
    model=patientmodel
    template_name='patientdelete.html'
    success_url=reverse_lazy('list_view')
    pk_url_kwarg='id'
    
class doctoredit(UpdateView):
    model=doctormodel
    template_name='docedit.html'
    success_url=reverse_lazy('doclist_view')
    pk_url_kwarg='id'
    form_class=doctorForm

class doctordelete(DeleteView):
    model=doctormodel
    template_name='docdelete.html'
    success_url=reverse_lazy('doclist_view')
    pk_url_kwarg='id'