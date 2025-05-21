def greet(message):
    def display():
        print(f"{message}");
    return display;
obj=greet("vk")
obj();