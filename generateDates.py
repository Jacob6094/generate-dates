from datetime import datetime, timedelta

start_date = datetime(1900, 1, 1)
end_date = datetime(2025, 12, 31)
current_date = start_date

with open("dates_wordlist.txt", "w") as f:
    while current_date <= end_date:
        f.write(current_date.strftime("%Y%m%d") + "\n")
        current_date += timedelta(days=1)
