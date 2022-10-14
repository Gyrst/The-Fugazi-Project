import requests, time, json
import pandas as pd

class TwitterIDFetcher:
    
    def __init__(self, usernames):
        """_summary_

        Args:
            usernames (DataFrame): reading the legislators.csv file as a pandas dataframe containing all the current US senators and representatives. It assumes the column with the ID has name "twitter"
            
        """
        self.twitter_ids = {}
        self.usernames = usernames.twitter.dropna()
        
    
    @staticmethod
    def fetch_id(username):
        return requests.post('https://tweeterid.com/ajax.php', data={"input":username})
    
    @staticmethod
    def format_username(username):
        return "@"+username
    
    def request_limit_warning(self, username, twitter_id, response, wait=30):
        print("--------------------------------------------------------")
        print("b'error was returned from the payload returned")
        print(response.status_code)
        print(username, twitter_id)
        print("hitting request limit")
        print("current set", self.twitter_ids)
        print("--------------------------------------------------------")
        time.sleep(wait)
    
    
    def to_json(self, output_file):
        with open(output_file, 'w') as reader:
            json.dump(self.twitter_ids, reader)
    
    def get_twitter_ids(self):
        for username in self.usernames:
            try:
                response_delivered = False
                username = self.format_username(username)
                response = self.fetch_id(username)
                while not response_delivered:
                    time.sleep(1/250)
                    if response.status_code==200:
                        response_delivered = True
                        twitter_id = response.content
                        if twitter_id == b'error':
                            self.request_limit_warning(username, twitter_id, response)
                            continue 
                        self.twitter_ids[username] = twitter_id
                        print("just added", username, twitter_id, "!")
                    else: 
                        print(response.status_code)
            except:
                print("Error occured with politician", username)  
                print("current fetched sample comprise", self.twitter_ids)  
            
        return self.twitter_ids
    
    