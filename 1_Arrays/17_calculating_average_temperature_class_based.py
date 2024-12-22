from time import sleep


class Temp:
    def __init__(self):
        self.temperatures = []

    def initialize_for_days(self, days):
        self.temperatures = [None] * days
        for i in range(days):
            temp = int(input(f"Give the high temperature for day {i + 1}\n"))
            self.add_day_temp(temp, i)

    def add_day_temp(self, temp, day):
        if len(self.temperatures):
            self.temperatures[day] = temp
            print(f"Updated the temperature for day {day + 1} to {temp} degrees.")
        else:
            print("Please initialize the temperature for days")

    def calculate_average_temperature(self):
        for i in range(21):
            if i == 10:
                string = " CALCULATING THE AVG TEMP "
            else:
                string = '#'
            sleep(0.2)
            print(string, end='')

        count = 0
        total_temp = 0
        for temp in self.temperatures:
            if temp:
                total_temp += temp
                count += 1
        if count:
            print(f"\n{total_temp / count} is the average temperature for {count} days")
            return
        print("You did not provide valid details to us.")
        return


temperature_test = Temp()
temperature_test.initialize_for_days(2)
temperature_test.calculate_average_temperature()
