from datetime import datetime, date

dateStr = "2010-8-9"
prevDate = datetime.strptime(dateStr, "%Y-%m-%d")

print(prevDate.weekday())

today = date.today()

datediff = today - date(prevDate.year, prevDate.month, prevDate.day)

print(datediff.days / 365)
