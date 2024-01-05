import os
from pwn import *

def check_bin_path(bin_path: str) -> bool:
    """バイナリファイルのパスの正当性チェック

    Args:
        bin_path (str): バイナリファイルのパス

    Returns:
        bool: バイナリファイルのパスが正しいかどうか
    """
    if bin_path == "":
        return False
    return os.path.isfile(bin_path)

def calc_offset_for_rip(rip_value: str) -> (int, bool):
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

if __name__ == "__main__":
    dst_bin_path = input("Specify destination binary file path: ")
    if not check_bin_path(dst_bin_path):
        print("specified path is invalid...")
        exit()

    proc = process(dst_bin_path)

    pattern_length = 1000
    pattern = cyclic(pattern_length)

    print("You copy this pattern and execute destination program")
    print(pattern.decode('utf-8' ))
    rip_value = input("When crashed RBP address: ")
    offset, result = calc_offset_for_rip(rip_value)
    if not result:
        print("Failed to calc offset...")
        exit()
    print("Succeed to calc offset!!")
    print(f"Offset for rip registers: {offset}")