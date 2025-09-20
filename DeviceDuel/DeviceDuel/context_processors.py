from django.conf import settings

def media_url(request):
    """ Make MEDIA_URL available globally in all templates """
    return {'MEDIA_URL': settings.MEDIA_URL}
