#!.env/bin/python3

from datetime import datetime, timedelta

working_hours = {
        'day_start': '09:00', 
        'day_end': '21:00'
        }

busy = [
        {'start': '10:30', 'stop': '10:50'},
        {'start': '18:40', 'stop': '18:50'},
        {'start': '14:40', 'stop': '15:50'},
        {'start': '16:40', 'stop': '17:20'},
        {'start': '20:05', 'stop': '20:20'},
        ]

free_time_schedule = []


def find_free_time(start, stop):
    start = datetime.strptime(start, '%H:%M')
    stop = datetime.strptime(stop, '%H:%M')
    visit_duration = timedelta(seconds=1800)
    free_time_duration = stop - start
    free_time_periods = free_time_duration // visit_duration
    for _ in range(free_time_periods):
        stop = start + visit_duration
        free_time_schedule.append({
            'start': datetime.strftime(start, '%H:%M'), 
            'stop': datetime.strftime(stop, '%H:%M')
            })
        start = stop


def main():
    busy_sorted = sorted(busy, key=lambda x: x['start'])
    find_free_time(working_hours['day_start'], busy_sorted[0]['start'])
    for idx in range(len(busy_sorted) - 1):
        find_free_time(busy_sorted[idx]['stop'], busy_sorted[idx+1]['start'])
    find_free_time(busy[-1]['stop'], working_hours['day_end'])
    return free_time_schedule


if __name__ == '__main__':
    main()



