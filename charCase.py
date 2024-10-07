class CustomString(str):

    def custom_method(self):
        # Add your custom methods here
        return f"Custom method called on {self}"
    
    # def toggle(self):

    



x = CustomString("Hello")
print(x.custom_method())
print(chr(ord("A") ^ 0b00100000))

























