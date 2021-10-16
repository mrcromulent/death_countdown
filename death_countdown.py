"""An idea to make your time on earth seem more valuable and fleeting?

TODO:
- Read out tasks from your calendar?
- Read out tips to extend your lifespan?
- Add semi-random fun facts about other lengths of time or lifespans?
"""


from datetime import date, timedelta
from gtts import gTTS
from playsound import playsound


save_location   = "morning.mp3"
user_name       = "Guy Incognito"
dob             = (1995, 1, 1)


def find_days_left():
    birth_date = date(*dob)
    life_expectancy = 82.5
    death_date = birth_date + timedelta(days=life_expectancy * 365)
    days_left = abs((death_date - date.today()).days)

    return days_left


def main():
    # The text that you want to convert to audio
    mytext = f"Good morning, {user_name}. " \
             f"You have approximately {find_days_left()} days left to live. " \
             f"Have a good one!"

    # Convert and play message
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save(save_location)
    playsound(save_location, True)


if __name__ == "__main__":
    main()
