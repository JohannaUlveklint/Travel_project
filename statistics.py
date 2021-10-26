import json
import datetime
from decimal import Decimal


class Statistics:
    def __init__(self):
        pass
    
    def calc_distance(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            meter = 0
            for line in data:
                meter += line['distance']
            distance = self.m_to_km(meter)
        return distance
    
    def calc_weekly_distance(self, week):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            meter = 0
    
            for line in data:
                if line['week'] == week:
                    meter += line['distance']
                    distance = self.m_to_km(meter)
                # if not all line['week'] != week:  # How do I check if logs from a certain week is missing?
                #     print('There are no logged trips from that week.')
                #     break
    
            return week, distance
    
    def m_to_km(self, meter):
            km = Decimal(meter / 1000).quantize(Decimal("1.000"))
            return km
    
    # def m_to_mil(self, meter):
    #         mil = Decimal(meter / 10000).quantize(Decimal("1.000"))
    #         return mil
    
    def calc_duration(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            seconds = 0
            for line in data:
                seconds += line['duration']
            duration = self.sec_converter(seconds)
        return duration
    
    def sec_converter(self, time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
        return time_without_ms
    
    
def main():
    statistics = Statistics()
    print(statistics.calc_distance())
    week, distance = statistics.calc_weekly_distance(18)
    print(f'Distance week {week}: {distance} km!')
    # print(statistics.calc_weekly_distance(18)[1])
    # print(calc_duration())

    # with open('test_statistics.wifm', 'r', encoding='utf-8') as json_file:
    #     data = json.load(json_file)
    #     distance = 0
    #
    #     for line in data:
    #         if line['week'] == '18':
    #             distance += line['distance']
    #             print(f'Distance week 18: {distance} km!')
    #         elif line['week'] == '19':
    #             distance += line['distance']
    #             print(f'Distance week 19: {distance} km!')
    #

#     data = json.load(json_file)


if __name__ == '__main__':
    main()
