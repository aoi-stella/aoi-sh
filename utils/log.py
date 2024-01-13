from utils.style import FontStyle
    
class Log:
    """Logクラス
    """
    INFO = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3
    
    @staticmethod
    def __get_title(level: int) -> str:
        """タイトルを取得する

        Args:
            level (int): ログレベル

        Returns:
            str: タイトル
        """
        title_dict = {
            Log.INFO: f'{FontStyle.info("[+INFO+]")}',
            Log.DEBUG:  f'{FontStyle.debug("[+DEBUG+]")}',
            Log.WARNING:  f'{FontStyle.warning("[+WARNING+]")}',
            Log.ERROR:  f'{FontStyle.error("[+ERROR+]")}'
        }
        
        if not level in title_dict:
            return
        return title_dict[level]
    
    @staticmethod
    def __info(message: str) -> None:
        """INFOレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{Log.__get_title(Log.INFO)} {message}')

    @staticmethod
    def __debug(message: str) -> None:
        """DEBUGレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{Log.__get_title(Log.DEBUG)} {message}')

    @staticmethod
    def __warning(message: str) -> None:
        """WARNINGレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{Log.__get_title(Log.WARNING)} {message}')
    
    @staticmethod
    def __error(message: str) -> None:
        """ERRORレベルログを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{Log.__get_title(Log.ERROR)} {message}')

    @staticmethod
    def log(level: int, message: str) -> None:
        """ログを出力する

        Args:
            level (int): ログレベル
            message (str): メッセージ
        """
        log_dict = {
            Log.INFO: Log.__info,
            Log.DEBUG: Log.__debug,
            Log.WARNING: Log.__warning,
            Log.ERROR: Log.__error
        }
        if not level in log_dict:
            Log.__error(f'Invalid level: {level}')
            return
        log_dict[level](message)