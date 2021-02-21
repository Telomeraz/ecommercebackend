from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny


class Authentication:
    """
    If request.method is GET method, then no auth needed otherwise uses an
    authentication
    """

    def get_authenticators(self):
        if self.request.method == "GET":
            return
        return (BasicAuthentication(),)


class DefaultSuperuserPermission:
    """
    If request method is one of admin_methods, allows only admin users
    otherwise allows anyone.
    """

    def get_permissions(self):
        if self.request.method in self.admin_methods:
            return (IsAdminUser(),)
        return (AllowAny(),)
