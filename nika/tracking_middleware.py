from django.utils .deprecation import MiddlewareMixin
from .models import Visitor 

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '<unknown>')

        Visitor.objects.create(
            ip_address = ip_address,
            user_agent = user_agent,
            path = request.path,
            
        )