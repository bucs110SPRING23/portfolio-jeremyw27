import requests

class Bored:
    def __init__(self):
        """
        Initializes the API url for Bored.
        args: none
        return: none
        """
        self.url = "http://www.boredapi.com/api/activity"
    
    def get(self, category):
        """
        Generates a random activity related to the type of the activity that the user picks.
        args: category (str)
        return: Random activity associated with the category that the user picks (str)
        """
        self.category = category
        r = requests.get(f"{self.url}?type={self.category}")
        response = r.json()
        if response.get("type") == self.category:
            return response["activity"] + "!"
        else:
            return "Sorry, type of activity is not available. Please try again."
        
    def __str__(self) -> str:
        """
        Returns object in string representation.
        args: none
        return: string
        """
        activity = self.get(self.category)
        return f"Activity Type: {self.category}\nActivity: {activity}"