from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


urlpatterns = [
    path("compare/",views.compare_Page,name="compare"),
    path("compare_selected/",views.compare_selected_handler,name="compare_selected_handler"),
    path("compare-selected/view/",views.Product_Details,name="Product_Details")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)