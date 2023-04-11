import time

# \r carriage return -> moves what is in front, to the beginning of the line

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print("\r", timer, end="")  # overrides the line with the ned timer
        time.sleep(1)
        t -= 1

    print('\nTimer completed')


t = input("Enter the time in seconds: ")

countdown(int(t))
