from django.shortcuts import render, redirect

# Create your views here.

from home.models import Outcome, Patient
from .forms import RegisterForm
from django.views import generic

def training(request):
	"""View function for training page of site."""
	context = {}
	return render(request, 'training.html', context=context)

    # Render the HTML template index.html with the data in the context variable


def index(request):
    """View function for home page of site."""
    
    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")

	else:
		form = RegisterForm()
	return render(request, "register.html", context={"form":form})

from django.contrib.auth.mixins import LoginRequiredMixin

class PatientsListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing patients added by the current user."""
    model = Patient
    template_name ='home/patient_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Patient.objects.order_by('date_contacted')

# Code for generating patient detail page

class PatientDetailView(generic.DetailView):
    model = Patient

# Code to generate page which lists the patients added by the user

class PatientsAddedByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing patients added by the current user."""
    model = Patient
    template_name ='home/patient_list_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Patient.objects.filter(contacted_by=self.request.user).order_by('date_contacted')

# Code to allow the user to create and edit patient info

from django.views.generic.edit import CreateView, UpdateView

class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = '__all__'

class PatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = '__all__'

