user_name = input("Enter your name: ")
message1 = "Hello %s!" % user_name  # for v.3 and v.2
message2 = f"Hello {user_name}!"  # for v.3.6 or later
print(message1)
print(message2)
