def WEEK(DAYS: int) -> str:
    match DAYS:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"

print(WEEK(5))
print(__name__)

if __name__ == "__main__":
    print("we are directly run the code")
    WEEK
    print(__name__)