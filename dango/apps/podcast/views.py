from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Episode, Host


class PodcastListView(ListView):
    queryset = Episode.objects.filter(status=1).order_by('-created')
    paginate_by = 3
    template_name = 'index.html'


class PodcastDetailView(DetailView):
    model = Episode
    template_name = 'podcast_detail.html'
