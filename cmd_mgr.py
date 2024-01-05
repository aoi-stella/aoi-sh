from observers.observer_frame import AbstractObserver

class CmdMng:
    def __init__(self):
        """初期化
        """
        self.mode = -1
        self.observers = []

    def set_mode(self, mode: int):
        """モードを設定する

        Args:
            mode (int): モード
        """
        self.mode = mode
        self.notify()
        
    def add_observer(self, new_observer: AbstractObserver):
        """オブザーバーを追加する

        Args:
            new_observer (AbstructObserver): 追加するオブザーバー
        """
        self.observers.append(new_observer)
        
    def notify(self):
        """オブザーバーに通知する
        """
        for observer in self.observers:
            observer.update(self.mode)