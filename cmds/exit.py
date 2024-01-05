from observers.observer_frame import AbstractObserver

class ExitObserver(AbstractObserver):
    def __proc(self):
        exit()
        
    def update(self, mode):
        """通知受信時更新処理

        Args:
            mode (int): モード
        """
        if mode == 0:
            print("Exit")
            self.__proc()