# logger
the best simple method to add logging for your python script


# Usage | Example
```
import logger

good = logger.Good(FILENAME="good.log", FILEMODE="a", TIME=True, DEBUG_MODE=True)
bad = logger.Bad(FILENAME="bad.log", FILEMODE="a", TIME=True, DEBUG_MODE=True)

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

try:
    print(math.sqrt(-1))
except Exception as e:
    print("ERROR:", e)
    bad.CRITICAL(e)
```

# `logger.Good`
has 
  1. SUCCESS
  2. COMPLETED
  3. DONE
  4. PASS
  5. LOADED
  6. IMPORTED

# `logger.Bad`
has
  1. CRITICAL
  2. ERROR
  3. WARNING
  4. INFO




