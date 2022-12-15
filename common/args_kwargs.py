def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


data1 = [10, 2, 5]
data2 = {"arg1": 3, "arg2": 32, "arg3": 4}
data20 = {"name": 3, "age": 32, "gender": 4}

# unpack with *
func1(*data1)
func2(*data2)

# unpack with **
func2(**data2)
# func2(**data20)  # error, not match "arg1"
