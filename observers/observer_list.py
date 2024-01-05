from observer_frame import AbstructObserver

class FindRIPOffsetObserver(AbstructObserver):
    """RIPまでのオフセットを計算するモードで使用するオブザーバークラス
    """
    def update(self, mode):
        """通知受信時更新処理

        Args:
            mode (int): モード
        """
        if mode == 1:
            print("Find offset for RIP")
            
class ExploitBOFObserver(AbstructObserver):
    """BOFを利用してExploitするモードで使用するオブザーバークラス
    """
    def update(self, mode):
        """通知受信時更新処理

        Args:
            mode (int): モード
        """
        if mode == 2:
            print("Exploit BOF")
            
if __name__ == "__main__":
    """Observerの動作確認テスト
    """
    chk_find_rip_offset = FindRIPOffsetObserver()
    chk_exploit_bof = ExploitBOFObserver()