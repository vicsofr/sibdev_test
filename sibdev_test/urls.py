from django.urls import path, include


urlpatterns = [
    path('deals/', include('deals.urls')),
]
