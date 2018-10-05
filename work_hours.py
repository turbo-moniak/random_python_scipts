import datetime


def calculate_time_at_work():
    current_time = datetime.datetime.now()

    start_hour = 9
    start_minute = 45
    hour = 60

    work_hours = current_time.hour - start_hour
    work_minutes = current_time.minute - start_minute

    if current_time.minute - start_minute < 0:
        work_hours -= 1
        work_minutes = hour + work_minutes

    return "Today you have worked: " + str(work_hours) + " hours and " + str(work_minutes) + " minutes"
    #test


if __name__ == "__main__":
    print(calculate_time_at_work())
