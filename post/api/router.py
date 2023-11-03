from rest_framework.routers import DefaultRouter
from post.api.views import PostView
router_post = DefaultRouter()

router_post.register(prefix="post", basename="post", viewset=PostView)