'''import calendar

print(calendar.month(2023, 5))
print(calendar.isleap(2020))
print(calendar.leapdays(2000, 2025))
print(calendar.weekday(2023, 5, 17))
print(calendar.monthrange(2023, 5))
print(calendar.prcal(2023))
print(calendar.calendar(2023))
print(calendar.monthcalendar(2023, 5))'''

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)    
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

import os

'''print(os.name)
print(os.getcwd())
print(os.listdir())
print(os.mkdir("new_folder"))
print(os.rmdir("new_folder"))
print(os.rename("old_name.txt", "new_name.txt"))
print(os.path.join("folder", "subfolder", "file.txt"))
print(os.path.split("folder/subfolder/file.txt"))
print(os.path.splitext("file.txt"))
print(os.path.getsize("new_name.txt"))
print(os.environ)
print(os.system("echo Hello, World!"))'''

import random
print(random.randint(1, 100))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.random())
print(random.uniform(1.0, 10.0))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.sample(range(100), 5))
print(random.seed(42))
print(random.getrandbits(8))
print(random.randrange(0, 101, 5))

import statistics

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
print(statistics.stdev(data))
print(statistics.variance(data))
print(statistics.harmonic_mean(data))
print(statistics.geometric_mean(data))
print(statistics.quantiles(data, n=4))





