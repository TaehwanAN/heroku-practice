import requests

def request_test():
  print("Hello")
  res = requests.get(url="https://my-development-app-6482cbf3b808.herokuapp.com/")
  print(res)

if __name__=="__main__":
  request_test()