from django.urls import path, include
from authentication.routes.user import Registration, LogOut
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('signup/', Registration.as_view(), name='signup'),
    path('logout/', LogOut.as_view(), name='logout')
]
