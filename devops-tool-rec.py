skill = input("enter your skill: ")
if skill == "automation":
    print("use ansible.")
elif skill == "monitoring":
    print("use prometheus")
elif skill == "container":
    print("use docker")
elif skill == "cloud":
    print("use aws")
else:
    print("skill not recognized.")
