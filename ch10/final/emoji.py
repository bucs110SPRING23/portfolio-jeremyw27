import requests

class Emoji:
    def __init__(self):
        """
        Initializes the API url for EmojiHub.
        args: none
        return: none
        """
        self.url = "https://emojihub.yurace.pro/api/random/group/face-positive"
    
    def get(self):
        """
        Gets a random emoji from the group of positive face emojis and displays it via unicode.
        args: none
        return: none
        """
        r = requests.get(self.url)
        response = r.json()
        unicode = response["unicode"]
        unicode = unicode[0].replace("+", "000")
        unicode = f"\{unicode}"
        self.emoji = unicode.encode('raw-unicode-escape').decode('unicode-escape')
        return self.emoji

    def __str__(self) -> str:
        """
        Returns object in string representation.
        args: none
        return: string
        """
        emoji = self.emoji
        return f"Emoji:{emoji}"