from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import users, user, owners, owner

urlpatterns = [
    path('users/', users, name="users_list_create"),
    path('users/<id>', user, name="userdetails"),
    path('owners/', owners ,name="owner"),
    path('owners/<id>', owner, name="ownerdetails"),
    path('gettoken', obtain_auth_token),
]