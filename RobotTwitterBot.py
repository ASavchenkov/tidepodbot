import tweepy
import time
import sys
import requests
import RobotTwitterBotCredentials

class RobotTwitterBot:
    def __init__(self):
        self.credentials = RobotTwitterBotCredentials.RobotTwitterBotCredentials()
        self.auth = tweepy.OAuthHandler(self.credentials.CONSUMER_KEY, self.credentials.CONSUMER_SECRET)
        self.auth.set_access_token(self.credentials.ACCESS_KEY, self.credentials.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

        self.userhandle = "tidepotrobotmid"
        self.tidepodIdentifierHandle = "tidepodbot"
        self.debug = True

    def dPrint(self , s):
        if self.debug:
            print(s)

    def makeRequest(self , imagePath , message = ""):
        """
        Makes a request to the tidepodIdentifierHandle Twitter bot using the
        image path
        
        Returns the response of that twitter account, stripped of the @userhandle
        """
        #image = r"C:\Users\Saikiran\Pictures\tide-pods.jpg"
        sentStatus = self.sendMediaTweet(self.tidepodIdentifierHandle , imagePath , message)
        id_str = sentStatus.id_str
        recStatus = self.getReplyTweet(self.userhandle , int(float(id_str)))
        return recStatus.text.strip("@{} ".format(self.userhandle))

    def sendMediaTweet(self , username , image_name , message):
        """
        Sends media tweet to username with the image
        """
        message = "@{} {}".format(username , message)
        status = self.api.update_with_media(image_name , message)
        return status

    def getReplyTweet(self , username ,  tweet_id , trys = 10):
        """
        959731728620208128
        """
        userQuery = "@{}".format(username)
        status = None
        while(trys > 0):
            status = self.api.search(q = userQuery , since_id = tweet_id)
            if len(status) != 0:
                break
            else:
                self.dPrint("GetReplyTweet failed! Retrying...")
                time.sleep(20)
                trys -= 1
        if len(status) > 1:
            self.dPrint("status is longer than 1!")
            
        return status[0]
