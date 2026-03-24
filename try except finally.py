try:
    print(10/0)
except ZeroDivisionError:
    print("error occured")
finally:
    print("execution completed")