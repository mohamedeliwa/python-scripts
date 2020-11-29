import time
import subprocess


def take_input(current_time):
    'validating user input to be a number and above than 0'
    while True:
        try:
            user_input = input(
                f"Enter {current_time} in minutes(defaults to {'25' if current_time == 'study' else '5'}): ")
            # asigning 25 min as the default value in case the user didn't specify a time
            if user_input == '' and current_time == 'study':
                user_input = '25'
            elif user_input == '' and current_time == 'break':
                user_input = '5'
            mins = int(user_input)
            if mins > 0:
                return mins
            else:
                continue
        except Exception:
            continue


def start_timer(study_time, break_time, current_time):
    'starting the timer to calculate the studying and break times'
    while True:
        if current_time == 'study':
            print(f"\nStart {study_time//60} mins of Studying...\n")
            time.sleep(study_time)
            current_time = 'break'
            for i in range(7):
                time.sleep(0.5)
                # running a command in shell, to produce a beep sound
                subprocess.run(["echo -ne '\\007'"], shell=True)
        else:
            print(f"\nTake {break_time//60} mins as a Break...\n")
            time.sleep(break_time)
            current_time = 'study'
            for i in range(7):
                time.sleep(0.5)
                # running a command in shell, to produce a beep sound
                subprocess.run(["echo -ne '\\007'"], shell=True)


def main():
    try:
        # two value 'study' or 'break'
        current_time = 'study'
        # defaults to 25 minutes in seconds
        study_time = take_input('study') * 60
        # defaults to 5 minutes in seconds
        break_time = take_input('break') * 60

        start_timer(study_time, break_time, current_time)
        
    except KeyboardInterrupt:
        print("\nHave Fun..!\n")


main()
