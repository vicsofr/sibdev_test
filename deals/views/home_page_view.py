from django.shortcuts import render

from deals_test.settings import BASE_URL


def home_page_view(request):
    """
    Home page view with links to APIs
    """
    context = {
        "post_deals_csv_url": f"{BASE_URL}/deals/post_deals_csv",
        "get_top_clients_url": f"{BASE_URL}/deals/get_top_clients",
    }
    return render(request, 'home.html', context=context)
