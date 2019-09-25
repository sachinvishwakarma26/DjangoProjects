from django.http import JsonResponse
class JsonResponseMixin(object):
    def render_to_json_response(self,context,**kwargs):
        return JsonResponse(context,**kwargs)
