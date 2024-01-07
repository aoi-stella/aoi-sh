from cmd_mgr import CmdMng
from cmds.find_offset_for_rip_register import FindRIPOffsetObserver
from cmds.exit import ExitObserver
from utils.interactive import Interactive

def print_banner():
    """バナーを出力する
    """
    banner = """
                                                        
                                                        
                     ■              ■              ■  ■ 
                     ■              ■              ■  ■ 
     ■■  ■                          ■              ■  ■ 
    ■  ■ ■    ■■■■   ■         ■■■  ■ ■■■   ■■■■   ■  ■ 
   ■    ■    ■    ■  ■ ■■■■■■ ■   ■ ■■   ■ ■    ■  ■  ■ 
  ■    ■■    ■    ■  ■         ■    ■    ■ ■■■■■■  ■  ■ 
  ■   ■■     ■    ■  ■          ■■  ■    ■ ■       ■  ■ 
  ■  ■ ■ ■   ■    ■  ■        ■   ■ ■    ■ ■    ■  ■  ■ 
   ■■   ■     ■■■■   ■         ■■■  ■    ■  ■■■■   ■  ■ 
                                                        
                                                        
                                                        
    
    """
    print(banner)

def print_script_info():
    """スクリプト情報を出力する
    """
    Interactive.script_info("Version : 0.0.1")
    Interactive.script_info("Author  : aoi")
    Interactive.script_info("Github  : https://github.com/aoi-stella/aoi-sh")
    Interactive.script_info("License : ???")
    print("\n")
    return

def get_mode() -> int:
    """モードをユーザーから取得する

    Returns:
        int: モード
    """
    Interactive.separator()
    Interactive.instruct("Select script mode")
    Interactive.instruct("[0]. Exit")
    Interactive.instruct("[1]. Find offset for RIP")
    Interactive.instruct("[2]. Exploit BOF")

    mode = int(Interactive.wait_for_input("Specify mode: "))
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
    print_script_info()
    Interactive.message("Welcome to aoi shell")
    while True:
        cmd_mgr = CmdMng()

        mode = get_mode()
        if mode==0:
            exit()
        
        subscribe_obsever(cmd_mgr)
        cmd_mgr.set_mode(mode)

if __name__ == "__main__":
    entry()