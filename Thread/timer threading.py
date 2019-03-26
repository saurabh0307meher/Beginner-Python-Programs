import threading
def world():
    print("Hello World!!!!!!!")
    t = threading.Timer(2.0, world)
    t.start()
