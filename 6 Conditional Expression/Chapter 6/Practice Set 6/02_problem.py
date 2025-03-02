math = int(input("Enter math marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))

total_percentage = (100*(math + science + english))/300

if(total_percentage>=40 and math>=33 and science>=33 and english>=33):
        print("You Are Pass", total_percentage)

else:
        print("You Are Failed, Try Again Next Year", total_percentage)