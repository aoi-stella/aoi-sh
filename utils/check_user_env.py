import sys

class CheckUserEnvironment:
    """ユーザー環境のチェックを行うクラス
    """
    
    @staticmethod
    def check_python3_installed() -> bool:
        """Python3がインストールされているかどうかをチェックする

        Returns:
            bool: Python3がインストールされているかどうか
        """
        if sys.version_info[0] == 3:
            return True
        else:
            return False
        
    @staticmethod
    def check_pwontools_installed() -> bool:
        """pwontoolsがインストールされているかどうかをチェックする

        Returns:
            bool: pwontoolsがインストールされているかどうか
        """
        try:
            import pwn
            return True
        except:
            return False