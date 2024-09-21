# Create a class 'Time' and initialize it with hours and minutes.
# Create a method addTime() which should take two Time objects
# and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
class Time:
    def __init__(self,hours,minute):
        self.hours=hours
        self.minute=minute

    @staticmethod
    def addTime(t1,t2):
        t1_total_min=t1.hours*60+t1.minute
        t2_total_min=t2.hours*60+t2.minute

        total_min=t1_total_min+t2_total_min
        total_hours=total_min//60
        total_minute=total_min%60

        return Time(total_hours,total_minute)


    def displayTime(self):
        print(f"{self.hours} hours and {self.minute} minutes")

    def displayMinutes(self):
        total_min=self.hours*60+self.minute
        print(f"{total_min} minutes")


time1 = Time(2, 50)
time2 = Time(1, 20)

answer=Time.addTime(time1,time2)
answer.displayTime()
answer.displayMinutes()