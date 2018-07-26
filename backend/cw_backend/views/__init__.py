from .auth import routes as auth_routes
from .api import routes as api_routes
from .fb_auth import routes as fb_auth_routes


all_routes = [
    *auth_routes,
    *api_routes,
    *fb_auth_routes,
]
