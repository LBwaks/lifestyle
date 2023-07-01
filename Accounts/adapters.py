from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(self, request, socialaccount):
        # Redirect to the specified URL after successful social authentication
        return resolve_url(settings.LOGIN_REDIRECT_URL)

    def authentication_error(self, request, provider_id, error=None, exception=None, extra_context=None):
        if error == 'account_exists':
            # Redirect to the LOGIN_REDIRECT_URL when an account with the social email already exists
            return HttpResponseRedirect(resolve_url(settings.LOGIN_REDIRECT_URL))
        else:
            # Handle other authentication errors
            return super().authentication_error(request, provider_id, error, exception, extra_context)
