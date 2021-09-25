import datetime as dt
import os


class Bad:
    def __init__(self, FILENAME:str="logger.log", FILEMODE:str="a", TIME:bool=True, DEBUG_MODE:bool=True):

        self.now_time = dt.datetime.now()
        self.FILENAME = FILENAME
        self.FILEMODE = FILEMODE
        self.TIME = TIME
        self.DEBUG_MODE = DEBUG_MODE

        if not os.path.exists(FILENAME):
            with open(FILENAME, "w", encoding="utf-8") as fmake_notexist:
                if TIME:
                    fmake_notexist.write(f"{self.now_time} LOG FILE CREATED")
                else:
                    fmake_notexist.write(f"LOG FILE CREATED")


    def CRITICAL(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nCRITICAL: {self.now_time}: {message}")
                else:
                    file.write(f"\nCRITICAL: {message}")
        else:
            pass

    def ERROR(self, message):
        with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
            if self.TIME:
                file.write(f"\nERROR: {self.now_time}: {message}")
            else:
                file.write(f"\nERROR: {message}")
    
    def WARNING(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nWARNING: {self.now_time}: {message}")
                else:
                    file.write(f"\nWARNING: {message}")
        else:
            pass
    
    def INFO(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nINFO: {self.now_time}: {message}")
                else:
                    file.write(f"\nINFO: {message}")
        else:
            pass
    





