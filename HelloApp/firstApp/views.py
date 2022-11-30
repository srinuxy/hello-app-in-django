from django.http import HttpResponse
import json

def Index(request):
	msg = { 'Message':'Hello World!'}
 
	return HttpResponse(json.dumps(msg), content_type='application/json')

# Create your views here.