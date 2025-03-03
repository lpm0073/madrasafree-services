"A Middleweaer to redirect user who just sign up to donate"
import json
from django.shortcuts import redirect

class MadrasafreeMiddleware:
    """
    Class to create a Django Middleware
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        redirect_path = request.COOKIES.get('SHOW_DONATE', 'no')
        if redirect_path != 'no':
            if request.method == "GET" and request.path != '/auth/complete/google-oauth2/':
                response = redirect(json.loads(redirect_path)['url'])
                response.delete_cookie('SHOW_DONATE',path='/',domain='.madrasafree.com')
                return response

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if request.path == '/api/user/v2/account/registration/' and request.method == 'POST' and response.status_code == 200:
            user = request.user
            redirect_url = f"https://apps.madrasafree.com/donate?name={user.profile.name}&last_name={user.extrainfo.last_name}&email={user.email}&new=true"
            response.set_cookie('SHOW_DONATE',json.dumps({'url':redirect_url}),secure=True,max_age=86400,domain='.madrasafree.com',path='/')
#            payload = {"success":True,"redirect_url":redirect_url}
#            response.content = json.dumps(payload,indent=2).encode('utf8')

        return response
