from utils.interactive import Interactive
from utils.log import Log

if __name__ == "__main__":
    Interactive.instruct("aoi-shell")
    Log.log(Log.INFO, "Welcome to aoi shell")
    Log.log(Log.DEBUG, "Welcome to aoi shell")
    Log.log(Log.WARNING, "Welcome to aoi shell")
    Log.log(Log.ERROR, "Welcome to aoi shell")