
import helpers as h
import random
import pyjokes

print(pyjokes.get_joke())

message = "secret message"


result = h.secret_string(message)
print(result)

result = h.any_starts_with_secret(["test", "secret test"])
print(result)

result = h.is_prime_number(17)
print(result)

#my_num = random.randint(-10, 10)
#my_num = "This won't work"


try:
    my_num = input("Pick a number please:")
    my_num = int(my_num)
    x = 5 / my_num
    print(x)
except ZeroDivisionError as e:
    print("Can't divide by zero!")
    print(e)
except TypeError as e:
    print("Can't figure out how to divide those!")
    print(e)
except ValueError as e:
    print("You must enter an actual number!")
    print(e)
except:
    print("Sorry, something went wrong!")
print(my_num)
