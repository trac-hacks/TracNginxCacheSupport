from trac.core import *
from trac.web.api import IRequestFilter

class NginxCacheSupportModule(Component):
    """Allow Nginx to cache content for anonymous users."""

    implements(IRequestFilter)

    def pre_process_request(self, req, handler):
        if req.authname != 'anonymous':
            req.send_header('X-Accel-Expires', '0')
        
        return handler

    def post_process_request(self, req, template, data, content_type):
        return template, data, content_type
