
from controller import Robot,Camera,RangeFinder
import cv2
import time
import socket
import glob


robot = Robot()

timestep = int(robot.getBasicTimeStep())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #SOCK_STREAM -> TCP  ,  SOCK_DGRAM  -> UDP
server_address = ("192.168.1.40", 11000) #
sock.connect(server_address) #Istemciyi sunucuya baglar.

path = "D:/Programlar/Webots/vehicles/controllers/my_controller/plaka.png"

while robot.step(timestep) != -1:

    KinectColor=robot.getDevice("kinect color")
    KinectRange=robot.getDevice("kinect range")

    #camera ve rangefinder başlatıldı. timestep başlatmaları aynı olması için kullanılıyor
    Camera.enable(KinectColor,timestep)
    RangeFinder.enable(KinectRange,timestep)

        #aracın üzerindeki resmi getirir.
    Camera.getImage(KinectColor)
        #resmi kayıt eder. nerden kayıt edileceği,  kayıt türü, kaç tane kayıt
    Camera.saveImage(KinectColor,"plaka.png",100)

    image=cv2.imread("plaka.png")
    f = open(path,"rb")
    data = f.read()
    sock.sendall(data)
        #with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #    s.connect((HOST, PORT))
        #    s.send(data)
    
    time.sleep(2)
 
