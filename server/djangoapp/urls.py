# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),
    # Path for login
    path('login', views.login_user, name='login'),
    # Path for logout
    path('logout', views.logout_request, name='logout'),
    path('get_cars', views.get_cars, name='get_cars'),
    # Path for dealer reviews view
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>/', views.get_dealerships, name='dealerbyst'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='deldetl'),
    path('reviews/dealer/<int:dealer_id>/', 
         views.get_dealer_reviews, name='delrev'),
    # Path for add a review view
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
