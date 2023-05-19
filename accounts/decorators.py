from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/account/dashboard/')
        else:
            response = view_func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                return response
            else:
                # Handle the case when view_func doesn't return an HttpResponse
                return HttpResponse("Something went wrong.")

    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                response = view_func(request, *args, **kwargs)
                if isinstance(response, HttpResponse):
                    return response
                else:
                    # Handle the case when view_func doesn't return an HttpResponse
                    return HttpResponse("Something went wrong.")
            else:
                return HttpResponse('Unauthorized to view this page')

        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('/account/user/view')
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized to view this page')

    return wrapper_func