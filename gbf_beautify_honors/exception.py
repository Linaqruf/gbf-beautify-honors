class NoSolutionError(Exception):
    """Raised when there is no solution"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
