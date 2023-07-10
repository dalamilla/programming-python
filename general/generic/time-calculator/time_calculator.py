def add_time(start, duration, day=""):
  start_time = start.split()
  dur_time = duration.split()
  arr_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  star_arr = start_time[0].split(":")
  dur_arr = dur_time[0].split(":")

  hour = int(star_arr[0]) + int(dur_arr[0])
  min = int(star_arr[1]) + int(dur_arr[1])
  day = day.lower().title()

  if min > 59:
    hour += 1
    min = min - 60
  
  if len(str(min)) < 2:
    min = "0" + str(min)

  count_days = 0

  while hour > 12:
    hour = hour - 12
    if start_time[1] == "PM":
      count_days += 1
      start_time[1] = "AM"
    else:
      start_time[1] = "PM"

  if hour == 12:
    if start_time[1] == "PM":
      start_time[1] = "AM"
      count_days += 1   
    else:
      start_time[1] = "PM"   

  if day == "":
    new_time = f'{hour}:{min} {start_time[1]}'
  else:
    check_day = count_days
    index = arr_days.index(day)
    while check_day:
      index += 1
      if index >= len(arr_days):
        index = 0
      day = arr_days[index]
      check_day -= 1
    new_time = f'{hour}:{min} {start_time[1]}, {day}'

  if count_days > 1:
    new_time = new_time + f' ({count_days} days later)'
  
  if count_days == 1:
    new_time = new_time + f' (next day)'
  
  return new_time
