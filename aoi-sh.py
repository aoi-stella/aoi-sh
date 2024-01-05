from pwn import *

print("↓攻撃対象のバイナリファイルを指定してください↓")
dst_bin_path = input()

proc = process(dst_bin_path)

pattern_length = 1000
pattern = cyclic(pattern_length)

print("以下のパターンを使用してプログラムをGDBで実行し、クラッシュさせてください:")
print(pattern.decode('utf-8' + "\n"))

rip_value = input("クラッシュ時のRBP値: ")

# 入力された値を16進数に変換
rip_value = int(rip_value, 16)

offset = cyclic_find(rip_value)
print(f"計算されたオフセット: {offset}")