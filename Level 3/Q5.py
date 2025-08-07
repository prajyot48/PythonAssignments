class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t):
        total_minutes = self.minutes + t.minutes
        extra_hours = total_minutes // 60
        total_hours = self.hours + t.hours + extra_hours
        remaining_minutes = total_minutes % 60
        return Time(total_hours, remaining_minutes)

    def displayTime(self):
        print(f"Time is {self.hours} hour(s) and {self.minutes} minute(s)")

    def displayMinute(self):
        total = self.hours * 60 + self.minutes
        print(f"Total minutes: {total}")

t1 = Time(2, 50)
t2 = Time(1, 20)
t3 = t1.addTime(t2)
t3.displayTime()     
t3.displayMinute()  
