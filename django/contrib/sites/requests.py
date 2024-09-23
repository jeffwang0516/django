from django.core.exceptions import SuspiciousOperation
from django.utils.http import is_safe_url

class RequestSite:
    """
    A class that shares the primary interface of Site (i.e., it has ``domain``
    and ``name`` attributes) but gets its data from an HttpRequest object
    rather than from a database.

    The save() and delete() methods raise NotImplementedError.
    """

    def __init__(self, request):
        self.domain = self.name = request.get_host()
        self.validate_host(self.domain)

    def validate_host(self, host):
        # 檢查主機是否合法
        if not is_safe_url(url=f"http://{host}", allowed_hosts=None):
            raise SuspiciousOperation("Unsafe host")

    def __str__(self):
        return self.domain

    def save(self, force_insert=False, force_update=False):
        raise NotImplementedError("RequestSite cannot be saved.")

    def delete(self):
        raise NotImplementedError("RequestSite cannot be deleted.")
