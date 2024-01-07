import os
from pwn import *
from observers.observer_frame import AbstractObserver
from utils.log import Log
from utils.interactive import Interactive

class FindRIPOffsetObserver(AbstractObserver):
    """RIPまでのオフセットを計算するモードで使用するオブザーバークラス
    """
    
    def __check_bin_path(self, bin_path: str) -> bool:
        """バイナリファイルのパスの正当性チェック

        Args:
            bin_path (str): バイナリファイルのパス

        Returns:
            bool: バイナリファイルのパスが正しいかどうか
        """
        if bin_path == "":
            return False
        return os.path.isfile(bin_path)

    def __calc_offset_for_rip(self, rip_value: str) -> (int, bool):
        """クラッシュ時のRIP値からオフセットを計算する

        Args:
            rip_value (str): クラッシュ時のRIP値

        Returns:
            int: オフセット
        """
        # 入力された値を16進数に変換
        rip_value = int(rip_value, 16)

        offset = cyclic_find(rip_value)
        if offset <= 0:
            return offset, False
        return offset, True
    
    def __proc(self):
        dst_bin_path = Interactive.wait_for_input("Specify destination binary file path: ")
        if not self.__check_bin_path(dst_bin_path):
            Log.log(Log.ERROR, "Please specify valid path")
            exit()

        proc = process(dst_bin_path)

        pattern_length = 1000
        pattern = cyclic(pattern_length)

        Log.log(Log.WARNING, "Please verify that the security features of the specified binary executable are disabled by using checksec.sh. ")
        Log.log(Log.WARNING, "This step is crucial to ensure that the binary is in the appropriate state for further analysis or testing.")
        Interactive.message("You copy this pattern and execute destination program")
        Log.log(Log.INFO, pattern.decode('utf-8'))
        rip_value = Interactive.wait_for_input("RBP address:")
        offset, result = self.__calc_offset_for_rip(rip_value)
        if not result:
            Log.log(Log.ERROR, "Failed to calc offset...")
            exit()
        Interactive.message("Success to calc offset for RIP register")
        Log.log(Log.INFO, f"Offset for rip registers: {offset}")
        
    def update(self, mode):
        """通知受信時更新処理

        Args:
            mode (int): モード
        """
        if mode == 1:
            Log.log(Log.INFO, "Mode : Find offset for RIP")
            self.__proc()