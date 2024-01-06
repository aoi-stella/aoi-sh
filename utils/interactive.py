from utils.style import FontStyle

class Interactive:
    """インタラクティブモード用クラス
    """
    def instruct(message):
        """ユーザーに対して指示を出力する

        Args:
            message (str): メッセージ
        """
        print(f'{FontStyle.instruction_to_user()}[+INSTRUCT+] {message}')