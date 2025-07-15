# from django.http import HttpResponseBadRequest

# def ajax_required(f):
#     def wrap(request, *args, **kwargs):
#         if not request.is_ajax():
#             return HttpResponseBadRequest()
#         return f(request, *args, **kwargs)
#     wrap.__doc__=f.__doc__
#     wrap.__name__=f.__name__
#     return wrap

from django.http import HttpResponseBadRequest
from functools import wraps

def ajax_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return HttpResponseBadRequest("Bad request: AJAX required")
        return f(request, *args, **kwargs)
    return wrap
