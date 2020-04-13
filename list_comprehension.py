# by basic for loop
temp_s = [123, 456, 345, 785, 334, 651, 563]

new_tem_p = []
for tem_p in temp_s:
    new_tem_p.append(tem_p / 10)

print(new_tem_p)

# list comprehension
temps = [123, 456, 345, 785, 334, 651, 563]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

# List comprehension with if conditional
temps2 = [123, 456, 345, 785, -334, 651, 563]  # if we want to avoid -334 to be functioned

new_temps2 = [temp2 / 10 for temp2 in temps2 if temp2 != -334]
print(new_temps2)

# List comprehension with elseif conditional
temps_2 = [123, 456, 345, 785, -334, 651, 563]  # if we want to avoid -334 to be functioned

new_temps_2 = [temp_2 / 10 if temp_2 != -334 else 0 for temp_2 in temps_2]  # when we put a else if inside a list we
# have to put the conditional before the loop
print(new_temps_2)

# List comprehension with elseif conditional with basic loop
temp_s_ = [123, 456, 345, 785, -334, 651, 563]

new_tem_p_ = []
for tem_p_ in temp_s_:
    if tem_p_ != -334:  # when the items go through the loop if it's true it follows the function of  (tem_p_ / 10)
        # and go back to the blank list.
        new_tem_p_.append(tem_p_ / 10)
    else:  # when if condition is false means when -334 comes through the if it called as false according to the
        # condition tem_p_ != -334 then it goes to else end and end appends a 0 instead of that item.
        new_tem_p_.append(0)

print(new_tem_p_)
