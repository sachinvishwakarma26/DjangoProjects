from django.http import JsonResponse
class JsonResponseMinxin(object):
    def render_to_json_response(self,context,**kwargs):
        return JsonResponse(context,**kwargs)
