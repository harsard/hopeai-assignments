class MultipleFunctions:
    def subfields(self):
        message = (
            "Sub-fields in AI are:\n"
            "Machine Learning\n"
            "Neural Networks\n"
            "Vision\n"
            "Robotics\n"
            "Speech Processing\n"
            "Natural Language Processing"
        )
        return message

    def OddEven(self):
        num = int(input("Enter a Number: "))
        if num % 2 == 1:
            message = f"{num} is an odd number"
        else:
            message = f"{num} is an even number"
        return message

    def Elegible(self,age):
        print(f"Your age is {age}")
        if age < 21:
            message = "NOT ELIGIBALE"
        else:
            message = "ELIGIBLE"
        return message

    def percentage(self,sub1, sub2, sub3, sub4, sub5):
        print(f"Subject1 = {sub1}")
        print(f"Subject2 = {sub2}")
        print(f"Subject3 = {sub3}")
        print(f"Subject4 = {sub4}")
        print(f"Subject5 = {sub5}")
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print(f"Total: {total}")
        percentage = (total / 500) * 100
        return percentage

    def area(self,height, breadth):
        print(f"Height: {height}")
        print(f"Breadth: {breadth}")
        print("Area formula: (Height * Breadth) / 2")
        area = (height * breadth) / 2
        print(f"Area of Triangle: {area}")

    def perimeter(self,height1, height2, breadth):
         print(f"Height1: {height1}")
         print(f"Height2: {height2}")
         print(f"Breadth: {breadth}")
         print("Perimeter formula: Height1 + Height2 + Breadth")
         perimeter = height1 + height2 + breadth
         print(f"Perimeter of Triangle: {perimeter}")
    