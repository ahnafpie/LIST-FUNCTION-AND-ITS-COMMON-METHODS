first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

message1 = "Hello %s %s!" % (first_name, last_name) # for v.2.0 or v.3.0
message2 = f"Hello {first_name} {last_name}!" # for v.3.6.0 or later
print(message1)
print(message2)
