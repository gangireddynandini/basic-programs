wkd=input("enter a week name:")
match(wkd.lower()[0:3:]):
    case ("mon" | "tue" | "wed" | "thu" | "fri"):
        print("working day")
    case "sat":
        print("week end")
    case "sunday":
        print("holiday")
