def demo():
    a = "FBS"
    def innerfun():
        print("I am in innerfunction",a)
    return innerfun
res = demo()
print(res)
