from rest_framework.routers import DefaultRouter
from comments.api.views import CommentView

router_comment = DefaultRouter()
router_comment.register(prefix="comment", basename="comment", viewset=CommentView)