from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.houses.models import Properties

class HomeView(TemplateView):
    template_name = 'index.html'


class PropertyView(TemplateView):
    template_name = 'properties.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        properties = Properties.objects.all()
        context['properties'] = properties
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class AgentView(TemplateView):
    template_name = 'agent.html'