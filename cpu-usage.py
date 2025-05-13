usage = int(input("enter usage: "))
if usage > 90:
    print("high cpu usage alert.")
elif usage < 90 and usage > 50:
    print("cpu usage is normal.")
elif usage < 50 :
    print("cpu underutilized")
else:
    print("enter correct usage.")