from django.urls import path

from deals.views.get_top_clients import GetTopClientsView
from deals.views.post_deals_csv import UploadDealsCsvView


urlpatterns = [
    path('post_deals_csv/', UploadDealsCsvView.as_view()),
    path('get_top_clients/', GetTopClientsView.as_view()),
]
