from utils.color import Color
    
class Log:
    """Logクラス
    """
    INFO = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3
    
    def __init__(self) -> None:
        """コンストラクタ
        """
        self.log_dict = {
            Log.INFO: self.__info,
            Log.DEBUG: self.__debug,
            Log.WARNING: self.__warning,
            Log.ERROR: self.__error
        }
    
    def __get_title(self, level) -> str:
        """タイトルを取得する

        Args:
            level (int): ログレベル

        Returns:
            str: タイトル
        """
        title_dict = {
            Log.INFO: f'{Color.BLUE + Color.BOLD}[+INFO+]{Color.RESET}',
            Log.DEBUG:  f'{Color.GREEN + Color.BOLD}[+DEBUG+]{Color.RESET}',
            Log.WARNING:  f'{Color.YELLOW + Color.BOLD}[+WARNING+]{Color.RESET}',
            Log.ERROR:  f'{Color.RED + Color.BOLD}[+ERROR+]{Color.RESET}'
        }
        
        if not level in title_dict:
            return
        return title_dict[level]
    
    def __info(self, message):
        """INFOレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{self.__get_title(Log.INFO)} {message}')

    def __debug(self, message):
        """DEBUGレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{self.__get_title(Log.DEBUG)} {message}')

    def __warning(self, message):
        """WARNINGレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{self.__get_title(Log.WARNING)} {message}')
        
    def __error(self, message):
        """ERRORレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{self.__get_title(Log.ERROR)} {message}')

    def log(self, level, message):
        """ログを出力する

        Args:
            level (int): ログレベル
            message (str): メッセージ
        """
        if not level in self.log_dict:
            self.__error(f'Invalid level: {level}')
            return
        self.log_dict[level](message)

# 動作確認テスト
if __name__ == "__main__":
    log = Log()
    log.log(Log.INFO, "this is info")
    log.log(Log.DEBUG, "this is debug")
    log.log(Log.WARNING, "this is warning")
    log.log(Log.ERROR, "this is error")