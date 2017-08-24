# encoding=utf-8
day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturdat']

lengthArray = []
for day in day_of_week:
    lengthArray.append(len(day))

print lengthArray

# 上面等同於下面這行
print [len(day) for day in day_of_week]

day_of_week2 = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturdat')
print type(day_of_week), type(day_of_week2)
print [len(day) for day in day_of_week2]