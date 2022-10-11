from django.urls import path

from .views import *


app_name = 'main'
urlpatterns = [
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(),
                                     name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
                                     name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
]