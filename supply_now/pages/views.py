from django.views.generic import TemplateView

# Class chama home

class HomePageView(TemplateView):
    template_name = "home.html"


