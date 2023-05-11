from bored import Bored
from emoji import Emoji

def main():
    user_pref = (str(input("What type of activity are you interested in doing? Pick from:\n"+
                      "education, recreational, social, diy, charity, cooking, relaxation, music, busywork: "))).lower()
    event = Bored()
    emoji = Emoji()
    activity = event.get(user_pref)
    print(activity)

    if activity == "Sorry, type of activity is not available. Please try again.":
        return None
    else:
        get_emoji = emoji.get()
        print(get_emoji*3)
    
    print(event.__str__())
    print(emoji.__str__())

main()