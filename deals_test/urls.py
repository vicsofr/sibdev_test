from django.urls import path, include
from deals.views.home_page_view import home_page_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('deals/', include('deals.urls')),
]
