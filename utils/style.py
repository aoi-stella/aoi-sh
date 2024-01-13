from utils.color import Color

class FontStyle:
    @staticmethod
    def info(message: str) -> str:
        return f'{Color.BLUE + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def debug(message: str) -> str:
        return f'{Color.GREEN + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def warning(message: str) -> str:
        return f'{Color.YELLOW + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def error(message: str) -> str:
        return f'{Color.RED + Color.BOLD}{message}{Color.RESET}'

    @staticmethod
    def instruction_to_user(message: str) -> str:
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def wait_for_input_from_user(message: str) -> str:
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def message_to_user(message: str) -> str:
        return f'{Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def script_info(message: str) -> str:
        return f'{Color.MAGENTA + Color.BOLD}{message}{Color.RESET}'
    
    @staticmethod
    def separator() -> str:
        return f'{Color.BOLD}{"+" * 80}{Color.RESET}'