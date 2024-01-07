from cmd_mgr import CmdMng
from cmds.exit import ExitObserver
from utils.interactive import Interactive
from utils.check_user_env import CheckUserEnvironment
from utils.log import Log

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

def check_user_env() -> bool:
    """ユーザー環境をチェックする

    Returns:
        bool: ユーザー環境が正常かどうか
    """
    is_python_ok = CheckUserEnvironment.check_python3_installed()
    if not is_python_ok:
        Log.log(Log.ERROR, "Please install python3")
        return False
        
    is_pwntools_ok = CheckUserEnvironment.check_pwontools_installed()
    if not is_pwntools_ok:
        Log.log(Log.ERROR, "Please install pwntools")
        return False
    
    return True
    

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
    from cmds.find_offset_for_rip_register import FindRIPOffsetObserver
    cmd_mgr.add_observer(FindRIPOffsetObserver())
    cmd_mgr.add_observer(ExitObserver())
    return

def __init():
    """初期化処理
    """
    print_banner()
    print_script_info()
    if not check_user_env():
        exit()
    Interactive.message("Welcome to aoi shell")

def __proc():
    """メイン処理
    """
    while True:
        cmd_mgr = CmdMng()

        mode = get_mode()
        if mode==0:
            exit()
        
        subscribe_obsever(cmd_mgr)
        cmd_mgr.set_mode(mode)

def entry():
    """エントリーポイント
    """
    
    __init()
    __proc()

if __name__ == "__main__":
    entry()