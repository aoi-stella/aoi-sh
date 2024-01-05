from cmd_mgr import CmdMng
from cmds.find_offset_for_rip_register import FindRIPOffsetObserver
from cmds.exit import ExitObserver

def get_mode() -> int:
    """モードをユーザーから取得する

    Returns:
        int: モード
    """
    print("+====================+")
    print("Select script mode")
    print("[0]. Exit")
    print("[1]. Find offset for RIP")
    print("[2]. Exploit BOF")

    mode = int(input("Specify mode: "))
    return mode

def subscribe_obsever(cmd_mgr: CmdMng):
    """オブザーバーを登録する

    Args:
        cmd_mgr (CmdMng): コマンドマネージャー
    """
    cmd_mgr.add_observer(FindRIPOffsetObserver())
    cmd_mgr.add_observer(ExitObserver())
    return

def entry():
    """エントリーポイント
    """
    while True:
        cmd_mgr = CmdMng()

        mode = get_mode()
        if mode==0:
            exit()
        
        subscribe_obsever(cmd_mgr)
        cmd_mgr.set_mode(mode)

if __name__ == "__main__":
    entry()