from django.urls import path
from .views import register, login_user, logout_user, update

app_name = 'accounts'

urlpatterns = [
    path('', login_user, name='connexion'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('<int:user_code>/', update, name='update_user')
]