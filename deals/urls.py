from django.urls import path

from deals.views.upload_deals_csv import UploadDealsCsvView


urlpatterns = [
    path('upload_deals_csv/', UploadDealsCsvView.as_view())
]
