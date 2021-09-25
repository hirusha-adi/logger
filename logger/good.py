import datetime as dt
import os


class Good:
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


    def SUCCESS(self, message):
        with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
            if self.TIME:
                file.write(f"\nSUCCESS: {self.now_time}: {message}")
            else:
                file.write(f"\nSUCCESS: {message}")
    
    def COMPLETED(self, message):
        with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
            if self.TIME:
                file.write(f"\nCOMPLETED: {self.now_time}: {message}")
            else:
                file.write(f"\nCOMPLETED: {message}")
    
    def DONE(self, message):
        with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
            if self.TIME:
                file.write(f"\nDONE: {self.now_time}: {message}")
            else:
                file.write(f"\nDONE: {message}")
    
    def PASS(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nPASS: {self.now_time}: {message}")
                else:
                    file.write(f"\nPASS: {message}")
        else:
            pass
    
    def LOADED(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nLOADED: {self.now_time}: {message}")
                else:
                    file.write(f"\nLOADED: {message}")
        else:
            pass

    def IMPORTED(self, message):
        if self.DEBUG_MODE:
            with open(self.FILENAME, self.FILEMODE, encoding="utf-8") as file:
                if self.TIME:
                    file.write(f"\nIMPORTED: {self.now_time}: {message}")
                else:
                    file.write(f"\nIMPORTED: {message}")
        else:
            pass




