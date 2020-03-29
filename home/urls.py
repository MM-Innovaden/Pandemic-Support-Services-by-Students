from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('training/', views.training, name='training'),
	path('register/', views.register, name='register'),
	path('mypatients/', views.PatientsAddedByUserListView.as_view(), name='mypatients'),
	path('allpatients/', views.PatientsListView.as_view(), name='allpatients'),
	path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
]

# URLs to allow users to add patients

urlpatterns += [  
    path('patient/create/', views.PatientCreate.as_view(), name='patient_create'),
    path('patient/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient_update'),
]