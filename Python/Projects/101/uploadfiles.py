import dropbox
import os

class TransferData():
  def __init__(self, token):
    self.token = token
   
  def uploadFile(self, source, destination):
    db = dropbox.Dropbox(self.token)
    with open(source, 'rb') as f:
        db.files_upload(f.read(), destination)

def main():
  accesstoken = 'sl.A_IjpeBVqb5iqsCn3eN6W5blX_32UIZBp0C71LtmZCuJCwHss2FEEg3LrufI3sr7GA-IGACAIahy7IBYpjeFsFL4ILCismPQmcpNsddl56ytHVWrssdcs1HV7IBJYBld7DUEKtKyyCqK'
  transferdataobject = TransferData(accesstoken)
  sourceinput = input("Enter the full path of the file you want to upload: ")
  dropboxlocation = '/DBJohn101'
  transferdataobject.uploadFile(sourceinput, dropboxlocation)
  print("File Moved")

main()