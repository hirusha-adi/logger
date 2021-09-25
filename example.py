import logger

print("Made by @hirusha-adi | ZeaCeR#5641")

good = logger.Good(FILENAME="log\\good.log", FILEMODE="a", TIME=True, DEBUG_MODE=True)
bad = logger.Bad(FILENAME="log\\bad.log", FILEMODE="a", TIME=True, DEBUG_MODE=True)

try:
    num = int(input("Enter a number: "))
    print(99/num)
    print("SUCCESS")
    good.SUCCESS("Divided number by Zero")
except ZeroDivisionError:
    print("ERROR")
    bad.ERROR("Cannot divide number by Zero")
except Exception as e:
    print("ERROR:", e)
    bad.ERROR(e)

try:
    import nomodulewiththisname
    good.IMPORTED("nomodulewiththisname - success")
except ModuleNotFoundError:
    print("ERROR")
    bad.CRITICAL("No module named 'nomodulewiththisname'")

import math

try:
    print(math.sqrt(10))
    good.COMPLETED("Found the sqrt of 10")
except Exception as e:
    print("ERROR:", e)
    bad.ERROR(e)

try:
    print(math.sqrt(-1))
except Exception as e:
    print("ERROR:", e)
    bad.CRITICAL(e)