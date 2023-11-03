from rest_framework import permissions
from comments.models import Comment


class IsOwnerOrReadAndCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            user_id = request.user.pk
            comment_id = view.kwards['pk']
            comment = Comment.objects.get(pk=comment_id)

            if user_id == comment.user_id:
                return True

            return False

