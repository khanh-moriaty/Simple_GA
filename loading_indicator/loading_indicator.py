from sys import stdout
from threading import Timer


class LoadingIndicator:
    """Indeterminately print dots to terminal to indicate loading."""

    def __init__(self, message, time):
        self.time = time
        self.thread = Timer(self.time, self.handle_function)
        print(message, end='')

    @staticmethod
    def print_loading_dot():
        print('.', end='')
        stdout.flush()

    def handle_function(self):
        self.print_loading_dot()
        self.thread = Timer(self.time, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()
        print('\n', end='')
