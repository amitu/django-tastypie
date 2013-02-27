from django.conf import settings
from django.contrib import admin


if hasattr(settings, 'AUTH_APP') and settings.AUTH_APP in settings.INSTALLED_APPS and hasattr(settings, 'AUTH_USER_MODEL'):
    from tastypie.models import ApiKey

    class ApiKeyInline(admin.StackedInline):
        model = ApiKey
        extra = 0

    # Also.
    admin.site.register(ApiKey)
