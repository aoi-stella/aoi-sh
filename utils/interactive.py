from utils.style import FontStyle

class Interactive:
    """インタラクティブモード用クラス
    """
    def instruct(message):
        """ユーザーに対して指示を出力する

        Args:
            message (str): メッセージ
        """
        print(f'{FontStyle.instruction_to_user(f"[+INSTRUCT+] {message}")}')
        
    def wait_for_input(message):
        """ユーザーからの入力を待つ

        Args:
            message (str): メッセージ

        Returns:
            str: 入力された文字列
        """
        return input(f'{FontStyle.wait_for_input_from_user(f"[+RESPONSE+] {message}")}')
    
    def message(message):
        """メッセージを出力する

        Args:
            message (str): メッセージ
        """
        print(f'{FontStyle.message_to_user(f"[+MSG+] {message}")}')