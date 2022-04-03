from loguru import logger
import sys

Log = logger
Log.remove()

# Configure console logger
fmt = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <level>{message: <50}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
Log.add(sys.stdout, level="DEBUG", format=fmt, enqueue=True, backtrace=True, diagnose=True)

# Configure file logger
Log.add("loguru_{time:YYYYMMDD}.log", level="DEBUG", format=fmt, enqueue=True, backtrace=True, diagnose=True)

Log.debug("That's it, beautiful and simple logging!")
Log.info("That's it, beautiful and simple logging!")
Log.warning("That's it, beautiful and simple logging!")
Log.error("That's it, beautiful and simple logging!")
Log.critical("That's it, beautiful and simple logging!")

# try:
#     x = 1 / 0
# except Exception as e:
#     Log.exception(e)


@Log.catch()
def divbyzero(n):
    def nested_func():
        Log.debug("Log from inside function")

    nested_func()
    x = 1 / n


divbyzero(0)
