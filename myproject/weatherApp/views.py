from django.shortcuts import render
from django.views.generic.base import TemplateView
class homeview(TemplateView):
    template_name = "home.html"
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
# Create your views here.
