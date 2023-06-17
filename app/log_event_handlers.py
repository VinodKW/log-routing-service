import abc
import logging
from .models import Log

class Handler(metaclass=abc.ABCMeta):
    """
    Define an interface for handling requests.
    Implement the successor link.
    """

    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle_request(self, request):
        pass


class LoginHandler(Handler):
    """
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self, request):
        if request.data.get('event_name') == 'login':  # if can_handle:
            print("Login event handler started.")
            log = Log(user_id=request.data.get('user_id'), 
                      unix_ts=request.data.get('unix_ts'), 
                      event_name=request.data.get('event_name'))
            log.save()
            logging.info("Login event handler completed.")

        elif self._successor is not None:
            self._successor.handle_request(request)


class LogoutHandler(Handler):
    """
    Handle request, otherwise forward it to the successor.
    """

    def handle_request(self, request):
        if request.data.get('event_name') == 'logout':  # if can_handle:
            print("Logout event handler started.")

            log = Log(user_id=request.data.get('user_id'), 
                      unix_ts=request.data.get('unix_ts'), 
                      event_name=request.data.get('event_name'))
            log.save()
            logging.info("Logout event handler started.")

        elif self._successor is not None:
            self._successor.handle_request(request)


class DefaultHandler(Handler):
 
    """Default Handler: child class from AbstractHandler"""

    def handle_request(self, request):
        logging.info("No handler found.")


def get_event_handler(): 
    default_handler = DefaultHandler()
    login_handler = LoginHandler(default_handler)
    logout_handler = LogoutHandler(login_handler)
    return logout_handler
    