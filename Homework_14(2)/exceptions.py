class GroupLimitError(Exception):
    def __init__(self, message="Група перевищує ліміт у 10 студентів"):
        super().__init__(message)