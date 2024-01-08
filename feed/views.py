from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my thing'] = 'Whatsup blud'
        return context