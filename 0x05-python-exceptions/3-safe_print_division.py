def safe_print_division(a, b):
    result = 0
    try:
        result = (a / b)
        return(a / b)
    except ZeroDivisionError:
        result = "None"
        return("None")
    finally:
        print("Inside result:".format(), end='')
        print("{}".format(result))
