import datetime
from datetime import datetime as dt
import getpass

import ascii


class Ticket:
    # *** Enter 'start_time' in "HH:MM:SS" military time format ***
    #  'rate' and 'maximum' default is set. <-- useful to add these parameters in the case of special events or holidays
    def __init__(self, plate_num, start_time, rate=.001):
        self.plate_num = plate_num
        self.start_time = start_time
        # self.end_time = dummy value that will be replaced when driver pays
        self.rate = rate
        self.format_start_time = dt.strptime(str(self.start_time.replace(microsecond=0)), '%Y-%m-%d %H:%M:%S')

    # *** Enter 'end_time' in "HH:MM:SS" military time format ***
    def begin_checkout(self):
        card = getpass.getpass('Swipe/Insert/Tap your card: ')
        self.end_time = datetime.datetime.now().replace(microsecond=0)
        self.format_end_time = dt.strptime(str(self.end_time.replace(microsecond=0)), '%Y-%m-%d %H:%M:%S')
        self.total = (self.end_time - self.start_time).total_seconds() * self.rate
        self.print_receipt()

    def print_ticket(self):
        print(ascii.car_art)
        print(ascii.ticket_art)
        print(f"License Plate Number: {self.plate_num}")
        print(f"Enter: {self.start_time}")

    def print_receipt(self):
        print(ascii.receipt_art)
        print(f"License Plate Number: {self.plate_num}")
        print(f"Enter: {self.start_time}")
        print(f"Leave: {self.end_time}")
        print(f"Paid: ${self.total:.2f}")

