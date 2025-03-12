from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)

class UserPermissionMixin(PermissionRequiredMixin):
    permission_required = None  # Must be set in the CBV

    def has_permission(self):
        return self.request.user.has_perm(self.permission_required)

    def handle_no_permission(self):
        return redirect("book_list")


class LoggingMixin:
    """Mixin to log user actions."""
    def log_action(self, message):
        """Log messages with request user info."""
        if self.request.user.is_authenticated:
            user = self.request.user
            logger.info(f"{message} by {user}")
        else:
            logger.info(message)
