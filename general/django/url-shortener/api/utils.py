import socket
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def check_domain(url: str) -> bool:
    domain = urlparse(url).netloc
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return False
    return True


def check_url(url: str) -> bool:
    validate_url = URLValidator()
    try:
        validate_url(url)
    except ValidationError:
        return False
    return True
