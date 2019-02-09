class WorkWeek:
    def __init__(self):
        self.schedule = {
            'sunday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'monday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'tuesday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'wednesday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'thursday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'friday': {
                'morning': [],
                'evening': [],
                'night': []
            },
            'saturday': {
                'morning': [],
                'evening': [],
                'night': []
            }}

        self.rules = {}

    def __repr__(self):
        string_to_return = ''
        week = self.schedule
        for day in week.keys():
            string_to_return += day + ':\n'
            for shift_name, shift in week[day].items():
                string_to_return += '   ' + shift_name + ': '
                for worker in shift:
                    string_to_return += worker + ' '
                string_to_return += '\n'
            string_to_return += '\n'
        return string_to_return


work_week = WorkWeek()
work_week.schedule['sunday']['morning'] = ['guy', 'yarden']
work_week.schedule['wednesday']['evening'] = ['hadar', 'yarden']
print(work_week)
