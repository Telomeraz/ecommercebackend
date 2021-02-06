from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class Authentication:
    """
    Authenticates users.
    """

    authentication_classes = (BasicAuthentication,)


class SuperuserPermission:
    """
    Checks if superuser has permission to access
    """

    permission_classes = (IsAdminUser,)


class UserPermission:
    """
    Checks if user has permission to access
    """

    permission_classes = (IsAuthenticated,)
