from utils.color import Color

class FontStyle:
    @staticmethod
    def info(message):
        return f'{Color.BLUE + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def debug(message):
        return f'{Color.GREEN + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def warning(message):
        return f'{Color.YELLOW + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def error(message):
        return f'{Color.RED + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def instruction_to_user(message):
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def wait_for_input_from_user(message):
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def message_to_user(message):
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def script_info(message):
        return f'{Color.MAGENTA + Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def separator():
        return f'{Color.BOLD}{"+" * 80}{Color.RESET}'