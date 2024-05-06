class User:

  #hidden variable(s)
  __password = "Rocky123"

  def __init__(self, name, username, email):
    self.name = name
    self.username = username
    self.email = email

  def getName(self):
    print(self.name)
  
  def setName(self, name):
    if self.name:
      print("Your name has been changed from "+self.name+" to "+name+"!")
      self.name = name
    else:
      print("Your name has been set to "+name)
      self.name = name

  def getPassword(self):
    print(self.__password)

  def setPassword(self):
    verify = input("Enter old password: \n> ")
    if verify == self.__password:
      new = input("Enter new password: \n> ")
      print("You password has been changed to: "+new)
      self.__password = new
    else:
      print("Stop trying to hack into this account!!")



Rocky = User("Rocky", "Rocksarecool", "rocky@gmail.com")
Rocky.getName()
Rocky.setName("Roxy")
# print(Rocky.__password) AttributeError: 'User' object has no attribute '__password'
Rocky.getPassword()
Rocky.setPassword()
