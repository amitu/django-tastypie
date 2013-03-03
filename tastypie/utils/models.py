from django.core.exceptions import ImproperlyConfigured


# from Django 1.5, django.contrib.auth
def get_user_model():
    "Return the User model that is active in this project"
    from django.conf import settings
    from django.db.models import get_model

    try:
        app_label, model_name = settings.AUTH_USER_MODEL.split('.')
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    user_model = get_model(app_label, model_name)
    if user_model is None:
        raise ImproperlyConfigured("AUTH_USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL)
    return user_model
