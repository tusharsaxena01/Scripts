import instaloader as ins


class InstaProfileDownloader:
    def __init__(self):
        self.bot = ins.Instaloader()

    def profilePicDownloader(self, username: str, onlyProfilePicture: bool) -> None:
        try:
            self.bot.download_profile(username, profile_pic_only=onlyProfilePicture)
        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    username = input("Enter the username: @")
    onlyProfilePicture = input("Do you want to download Profile Picture only (Y\\N): ")
    if onlyProfilePicture in 'Yy':
        onlyProfilePicture = True
    else:
        print("Downloading Full Profile...")
        onlyProfilePicture = False
    print(onlyProfilePicture)
    InstaProfileDownloader().profilePicDownloader(username, onlyProfilePicture)
