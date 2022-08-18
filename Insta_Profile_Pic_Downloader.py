def profilePicDownloader(bot):
    username = input("Enter Instagram Username: @")
    bot.download_profile(username, profile_pic_only=True)
try:
    import instaloader as ins
    profilePicDownloader(ins.Instaloader())
except ModuleNotFoundError:
    print("Module Not Found!")
    ch = input("Install Now? (Y\\N): ")
    if 'Yy' in ch:
        import os
        os.system('pip install instaloader')
        import instaloader as ins
        profilePicDownloader(ins.Instaloader())
    else:
        print("Installation of module is required for the program to continue!")
except Exception as e:
    print("Error! Try Again!")
    print(e)
