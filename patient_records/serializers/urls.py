from django.urls import path

from .views import (
	CreatePatientDetailsAPIView,
	PatientsListAPIView,
	GetPatientDetailsAPIView,
	UpdatePatientDetailsAPIView,
	DeletePatientDetailsAPIView,
	StartNewSessionAPIView,
	SessionListAPIView,
	GetSessionDetailsAPIView,
	SessionLevelOneAPIView,
	SessionLevelTwoAPIView,
	SessionFinalLevelAPIView
	)

urlpatterns = [
    path('patient/new', CreatePatientDetailsAPIView.as_view()),
    path('patient/list', PatientsListAPIView.as_view()),
    path('patient/details/<int:pk>', GetPatientDetailsAPIView.as_view()),
    path('patient/update/<int:pk>', UpdatePatientDetailsAPIView.as_view()),
    path('patient/delete/<int:pk>', DeletePatientDetailsAPIView.as_view()),
    path('session/new', StartNewSessionAPIView.as_view()),
    path('session/list', SessionListAPIView.as_view()),
    path('session/details/<int:pk>', GetSessionDetailsAPIView.as_view()),
    path('session/details/stage-one', SessionLevelOneAPIView.as_view()),
    path('session/details/stage-two', SessionLevelTwoAPIView.as_view()),
    path('session/details/stage-three', SessionFinalLevelAPIView.as_view()),
	]
