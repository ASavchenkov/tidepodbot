import tweepy
import time
import sys
import requests
import RobotTwitterBotCredentials
import picamera
from PIL import Image

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

        image path can be a string or a list of strings
        
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
        status = None
        if type(image_name) == list:
            media_ids = []
            for filename in image_name:
                 res = self.api.media_upload(filename)
                 media_ids.append(res.media_id)
            status = self.api.update_status(status=message , media_ids=media_ids)
        else:
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

class CameraOp:
  def __init__(self):
    self.n=1000
    self.resolution = (2*self.n,self.n)
    self.camera = None
    
  def initCamera(self,timeToSleep=2):
    self.camera = picamera.PiCamera()  
    time.sleep(timeToSleep)
    self.camera.resolution = (2*self.n,self.n)
    
  def take_picture(self,filename):
    assert self.camera!=None #camera probably not init yet
    self.camera.capture(filename)
    
  def split_image(self,in_filename,out_filename_left,out_filename_right):
    in_im = Image.open(in_filename)

    im_left= im.copy().crop((0,0,self.n,self.n))
    im_right= im.copy().crop((self.n,0,2*self.n,self.n))
    
    with open(out_filename_left,'wb') as outfile:
      im_left.save(outfile, "JPEG")
    with open(out_filename_right,'wb') as outfile:
	    im_right.save(outfile, "JPEG")


if __name__=='__main__':
  co = CameraOp()
  Robot = RobotTwitterBot()
  co.initCamera()
  co.take_picture("ravi.jpg")
  Robot.makeRequest("ravi.jpg","ROLL TIDEEEE")
  
  
