import socket


def check_domain(domain: str):
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return False
    return True
