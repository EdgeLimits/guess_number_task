from django.urls import path
from api.views import GuessView


app_name = 'api'
urlpatterns = [
    path('', GuessView.as_view(), name='home'),
    # path('<str:slug>/', views.page_view, name='page_view'),
    # path('<str:slug>/edit/', views.page_edit, name='page_edit'),
    # path('<str:slug>/save/', views.page_save, name='page_save'),
]