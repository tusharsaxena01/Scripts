def profilePicDownloader(bot):
  username = input("Enter Instagram Username: @")
  bot.download_profile(username.profile, profile_pic_only=True)
try:
    import instaloader as ins
    profilePicDownloader(ins.Instaloader())
except ModuleNotFoundError:
    print("Module Not Found!")
    if 'Yy' in input("Install Now? (Y\N):"):
      import os
      os.system('pip install instaloader')
      import instaloader as ins
      profilePicDownloader(ins.Instaloader())
    else:
      print("Installation of module is required for the program to continue!")
except:
  print("Error! Try Again!")
