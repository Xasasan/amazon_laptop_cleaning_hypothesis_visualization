import time
def timer(func):
    def wrapper(mins):
        func(mins)
        time.sleep(mins)
        print(f"7 raqam maydonga qaytishi mumkun {mins} daqiqa tugadi")

    return wrapper



@timer
def remove_player(mins):
    print(f' 7 raqam maydondan {mins} daqiqaga chetlashtirildi')



mins = int(input('necha daqiqaga ?'))
remove_player(mins)
