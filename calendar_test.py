import calendar

# d = calendar.TextCalendar(calendar.MONDAY)

month = calendar.itermonthdates(2026,1)

for c in month:
  if c.weekday() == calendar.MONDAY:
    print(f"Mondays > '{c}")



# print(d.formatmonth(2026,1,0,0))