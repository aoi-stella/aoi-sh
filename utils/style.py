from utils.color import Color

class FontStyle:
    @staticmethod
    def info():
        return f'{Color.BLUE + Color.BOLD}'

    @staticmethod
    def debug():
        return f'{Color.GREEN + Color.BOLD}'

    @staticmethod
    def warning():
        return f'{Color.YELLOW + Color.BOLD}'

    @staticmethod
    def error():
        return f'{Color.RED + Color.BOLD}'

    @staticmethod
    def instruction_to_user():
        return f'{Color.BOLD}'