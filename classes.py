class MyColor:
    def __init__(self,color,comment):
        self.color = color
        self.comment = comment

    def myfunc(self):
        print("All colors are unique in their own special way like:" + self.color)

x1 = MyColor("blue," ,"I love Cyan shade of blue")
x2 = MyColor("green," ,"I love the Kelly shade of green")

print(x1.color)
print(x1.comment)
x1.myfunc()
print(" ")
print(x2.color ,x2.comment)
x2.myfunc()