from django.urls import path
from core import views
from .models import LogMessage


home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5], # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="core/home.html",
)
app_name='core'
urlpatterns = [
    
    path("home", home_list_view, name="home"),
    path("", views.visitor, name="visitor"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log")

]