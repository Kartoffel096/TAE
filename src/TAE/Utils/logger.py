"""Logger for Logging Stuff"""

# pylint: disable=W,E,C0301
import os
import inspect
import time
from datetime import datetime

# from TAE.Utils.tcolors import *
# from TAE.config import (
#     log_file,
#     logging,
#     consoleLogging,
#     fileLogging,
#     consoleLogLevel,
#     FileLogLevel,
#     LogByModule,
#     logLevels,
#     LogPrefix,
#     LogColors,
#     DefaultLogLevel,
#     ShowOnlyLogText,
# )
import TAE.config


class Logger:
    """Logger Class"""

    def log(
        text: str = "", errlvl: int = config.DefaultLogLevel
    ) -> int:  # pylint: disable=R1710
        """Logging function"""

        """
            Prints Debug Information into Console
        Args:
            text (str): Text to be Displayed. Defaults to "".
            errlvl (int): Errorlevel defined in config.py | Default to FileLogLevel.DefaultLogLevel in config.py.
        """

        if not config.logging:
            return
        module = inspect.currentframe().f_back.f_globals["__name__"]
        function = inspect.stack()[1].function
        line_number = inspect.stack()[1].lineno
        message = str(text)

        logmessage = Log(message, errlvl, module, function, line_number)

        if config.consoleLogging:
            if logmessage.loglevel >= config.consoleLogLevel:
                if FileLogLevel.ShowOnlyLogText:
                    print(logmessage.stronly)
                else:
                    print(logmessage)

        if config.fileLogging:
            if logmessage.loglevel >= FileLogLevel.consoleLogLevel:
                if FileLogLevel.LogByModule:  # pylint: disable=R1705
                    _log_file = config.log_file.split("/".replace(os.sep))
                    _log_file.insert(1, f"/{module} - ".replace(os.sep))
                    _log_file = "".join(_log_file)
                    with open(_log_file, "a") as log:
                        log.write(logmessage.raw)
                    return 0
                else:
                    with open(config.log_file, "a") as log:
                        log.write(logmessage.raw)
                    return 0
        return 1

    def time(func: callable) -> callable:
        """Timing Decorator Function

        Args:
            func (callable): Function which should be timed
        """

        def wrapper(*args, **kwargs) -> callable:
            start = time.time()
            val = func(*args, **kwargs)
            _time = time.time() - start
            if _time > 1:
                Logger.log(f"Functioncall: {func} took {_time}s to execute", 1)
            else:
                Logger.log(f"Functioncall: {func} took {_time}s to execute", 2)
            return val

        return wrapper


class Log:
    """Log Class"""

    __slots__ = (
        "logstr",
        "loglevel",
        "module",
        "function",
        "line_number",
        "timestamp",
        "raw",
        "stronly",
    )

    def __init__(
        self,
        logstr: str = "",
        loglevel: int = -1,
        module: str = None,
        function: str = None,
        line_number: int = None,
        raw: str = None,
        stronly: str = "",
    ) -> None:
        if module is None:
            module = ""
        if function is None:
            function = ""
        if line_number is None:
            line_number = ""
        if raw is None:
            raw = ""

        self.logstr = logstr
        """The Message that is being logged"""
        self.loglevel = loglevel
        """The Loglevel of the Log entry (-1=DBG;0=INFO;1=WARN;2=ERROR;3=FATAL)"""
        self.module = module
        """The Module from which the Message has been logged"""
        self.function = function
        """The function from which the Message has been logged"""
        self.line_number = line_number
        """The Line Number from which the Message was called"""
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        """The Timestamp of the logged Message"""
        self.raw = f"{self.timestamp} - [{self.line_number}] {FileLogLevel.logLevels[self.loglevel]} - {self.module} - {self.function}: {self.logstr}\n"
        """Logmessage in Raw format"""
        self.stronly = f"{FileLogLevel.LogColors[self.loglevel](self.logstr)}"
        """Colorized LogMessage Only"""

    def __str__(self) -> str:
        stack = f"[{self.line_number}] {FileLogLevel.logLevels[self.loglevel]:<7} - {self.module}.{self.function} : "
        return f"{FileLogLevel.LogPrefix[self.loglevel]} {FileLogLevel.LogColors[self.loglevel](stack)} {self.logstr}"
