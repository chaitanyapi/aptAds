from django.http import HttpResponseRedirect
from django.conf import settings
from re import compile
from django.contrib.auth import logout
from django.contrib import messages
import datetime
from django.shortcuts import redirect
from .models import Emp

#from django import settings
EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

"""
class SessionIdleTimeout:
    def process_request(self, request):
        if request.user.is_authenticated():
            current_datetime = datetime.datetime.now()
            if ('last_login' in request.session):
                last = (current_datetime - request.session['last_login']).seconds
                if last > settings.SESSION_IDLE_TIMEOUT:
                    logout(request, login.html)
            else:
                request.session['last_login'] = current_datetime
        return None
"""
class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).
    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        """, "The Login Required middleware\
 requires authentication middleware to be installed. Edit your\
 MIDDLEWARE_CLASSES setting to insert\
 'django.contrib.auth.middleware.AuthenticationMiddleware'. If that doesn't\
 work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
 'django.core.context_processors.auth'."""

        path = request.path_info.lstrip('/')

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if path == 'aptdata/logout/':
            logout(request)

        if request.user.is_authenticated() and url_is_exempt:
            #this will check the user role
            if Emp.objects.filter(emp_name=request.user.username).values('emp_dept')[0]['emp_dept'] == 'ADMIN':
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                return HttpResponse("Welcome buddy")

        elif request.user.is_authenticated() or url_is_exempt:
            return None

        else:
            # if not any(m.match(path) for m in EXEMPT_URLS):
            return HttpResponseRedirect(settings.LOGIN_URL)