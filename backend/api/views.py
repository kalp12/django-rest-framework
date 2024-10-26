import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    
    body = request.body
    # print(body)
    data = {}
    try:
        data = json.loads(body)

    except:
        pass
    data['headers'] = request.headers
    data['content_type'] = request.content_type
    data['params'] = request.GET
    print(data)
    
    return JsonResponse({'message': 'Hi there'})
