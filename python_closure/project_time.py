import datetime

def project(projectTimeSlot):
   time = projectTimeSlot
   now = datetime.datetime.now()
   
   def addTime():
       nonlocal time
       time = time + 1
       print(time)

   def projectEndTimeCalculator():
       if((time + now.hour) < 24):
           print("will be finished by {} hour(s) later".format(time + now.hour))
       else:
           daysLater = (time + now.hour) % 24
           print("will be finished by {} day(s), {} hour(s) later".format(daysLater, (time + now.hour) / 24))

   return addTime 

if __name__ == '__main__':
   myProject = project(10)
   myProject()
   myProject()
   myProject()
