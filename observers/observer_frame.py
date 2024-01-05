import abc

class AbstructObserver(metaclass=abc.ABCMeta):
    """Observerの抽象クラス

    Args:
        metaclass (_type_, optional): Defaults to abc.ABCMeta.
    """
    @abc.abstractmethod
    def update(self):
        """通知受信時更新処理
        """
        pass
