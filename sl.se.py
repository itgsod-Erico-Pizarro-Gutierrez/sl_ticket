def fares(age, student=False, senior=False):
    print age, student,senior
    if age <=18:
        return 'halv'
    elif age >=64:
        return 'halv'
    else:
        return 'hel'






print 'barn 11',fares(11)
print 'pension 63',fares(63)
print 'student 25', fares(25,student=True)
print 'vuxen 45',fares(45)