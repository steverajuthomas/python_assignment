# Physics,Chemistry, Biology, Mathematics, and Computer

Physics = int(input("input marks received for Physics "))
Chemistry = int(input("input marks received for Chemistry "))
Biology = int(input("input marks received for Biology "))
Mathematics = int(input("input marks received for Mathematics "))
Computer = int(input("input marks received for Computer "))

avg_score = (Physics+Chemistry+Biology+Mathematics+Computer)/5

if avg_score>= 90:
    print("Grade A")
elif avg_score>= 80:
    print("Grade B")
elif avg_score>= 70:
    print("Grade C")
elif avg_score>= 60:
    print("Grade D")
elif avg_score>= 40:
    print("Grade E")
else:
    print("Grade F")

