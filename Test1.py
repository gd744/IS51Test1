"""
This programe will determine which salary payment option is superior. 
OPTION 1 is a payment of 100 dollars per day for 10 days. 
OPTION 2 starts at a dollar per day, but doubles each day for 10 days. 
Two different functions will calculate each option.
The first function will calculate OPTION1, multiplying 100 dollars * 10 days.
The second option will calculate OPTION2, using 10 loops to calulate the doubling scaling wage. 
If OPTION1 and OPTION2 are equal, user output will read "Both Options pay the same"
If OPTION 1 is greater, output will read "Option1 pays more"
If OPTION 2 is greater output will read "Option2 pays more"
"""
# PSUEDOCODE
# Option1
#     return 100 * 10
# Option 2
#     amount = 1
#     list1 = []
#     loops 10 times
#         adds amount to list1
#         amount doubles, *=2
#         reads = sum of all items in loop
#     return sum
# main()
#     var1 = Option1
#     var2 = Option2
#     if var1 = var2
#         print "Both options pay the same."
#     if var1 < var2
#         print "Option 2 pays more"
#     else
#         "Option 1 pays more"


def option1():
    return 100 * 10


def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total


def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Both Options Pay the Same"
    elif var1 < var2:
        answer = "Option 2 pays more"
    else:
        answer = "Option 1 pays more"
    print(answer)
main()