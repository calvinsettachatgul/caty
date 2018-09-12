# def outerFunction(text):
#     text = text
#  
#     def innerFunction():
#         print(text)
#  
#     innerFunction()
# 
# outerFunction("hidden word")

def clock(start):
    time = start
    print(time)
     
    def increment_clock():
        nonlocal time
        time = time + 1
        return time
    # def increment_clock():
    #     time = time + 1
    #     return time
    return increment_clock 

timer = clock(0)
print(timer())
print(timer())

# def make_multiplier_of(n):
#     def multiplier(x): 
#         return x * n
#     return multiplier
    
# times3 = make_multiplier_of(3) 

# print(times3(3))