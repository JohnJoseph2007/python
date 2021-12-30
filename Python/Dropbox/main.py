import dropbox

class GivingData():
  def __init__(self, token):
    self.token = token

  def upload(self, source, destination):
    db = dropbox.Dropbox(self.token)
    with open(source, 'rb') as i:
      db.files_upload(i.read(), destination)

def main():
  accesstoken = "sl.A_KkySOZvCcW9KMmSGZqb9NhX7Gb4jSFil_Yrga7QUomCwSPPq8oI8bK0v2UKNn6mlIyyVHxDb1fzOiJ3xJ2P-N_bewuqD--2U1_Wkk5a30qc6nWJBmyn5rvwLQuZpjemquuE8yZUKKg"
  objectofclass = GivingData(accesstoken)
  s = "Dante.png"
  d = "/DBJohn1"
  objectofclass.upload(s, d)
  print("File has been moved")

main()