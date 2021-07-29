from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PodcastPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin
class PodcastPluginPublisher(CMSPluginBase):
    model = PodcastPluginModel
    module = _("Podcast")
    name = _("Podcast Plugin")
    render_template = "podcast_cms_integration/podcast_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
