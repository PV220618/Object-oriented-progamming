from library_item import LibraryItem


library = {}

library["01"] = LibraryItem("TIM ANH GHEN", "Wxrdie", 5)
library["02"] = LibraryItem("GET MONEY", "Wxrdie", 5)
library["03"] = LibraryItem("DATLE", "B-wine", 5)
library["04"] = LibraryItem("On the way", "B-Wine", 5)
library["05"] = LibraryItem("QUA TỪNG KHUNG HÌNH", "Robber ft NGẮN", 5)
library["06"] = LibraryItem("SSREMEMBER", "Pjpo BlackBi Zin9 BốDu YoungH Torai9 BabyRed Kiban LJ Eszi S.O S-Fury Phutoro", 5)
library["07"] = LibraryItem("ĐÂU PHẢI VỢ ANH", " Dangrangto", 4)
library["08"] = LibraryItem("Dại Kher", "Sony Tran ft Tage , Blacka", 4)
library["09"] = LibraryItem("Welcome to the Show", "Bray", 5)
library["10"] = LibraryItem("TALAGI", "kidsai ft Dangrangto", 4)

library["11"] = LibraryItem("Glock In My Lap", "21 Savage & Metro Boomin", 5)
library["12"] = LibraryItem("Runnin", "21 Savage & Metro Boomin", 5)
library["13"] = LibraryItem("a lot", "21 Savage ft J Cole", 5)
library["14"] = LibraryItem("Thời Tiết Rất Lạnh Vào Ngày Hôm Nay", "Robber ft Winno", 4)
library["15"] = LibraryItem("Not Enough", "Robber", 4)
library["16"] = LibraryItem("Trên Chuyến Bay", "Robber ft YFT Luci", 4)
library["17"] = LibraryItem("Say Wazzup", "Robber", 5)
library["18"] = LibraryItem("His Story", "Robber", 5)
library["19"] = LibraryItem("Vô Định", "Robber", 5)
library["20"] = LibraryItem("See You Again", "Wiz Khalifa ft. Charlie Puth", 5)

library["21"] = LibraryItem("Not Like Us", "Kendrick Lamar", 4)
library["22"] = LibraryItem("Sunflower", "Post Malone & Swae Lee", 5)
library["23"] = LibraryItem("Love Yourself", "Justin Bieber", 4)
library["24"] = LibraryItem("Rockstar", "Post Malone ft. 21 Savage", 3)
library["25"] = LibraryItem("Hello", "Adele", 5)
library["26"] = LibraryItem("Sorry", "Justin Bieber", 4)
library["27"] = LibraryItem("HUMBLE.", "Kendrick Lamar", 5)
library["28"] = LibraryItem("One Dance", "Drake ft. Wizkid & Kyla", 4)
library["29"] = LibraryItem("Cheap Thrills", "Sia ft. Sean Paul", 4)
library["30"] = LibraryItem("FE!N", "Travis Scott ft Playboi Carti", 5)

library["31"] = LibraryItem("", "Dua Lipa", 5)
library["32"] = LibraryItem("APT", "ROSÉ & Bruno Mars", 5)
library["33"] = LibraryItem("We Will Rock You", "Queen", 4)
library["34"] = LibraryItem("Billie Jean", "Michael Jackson", 5)
library["35"] = LibraryItem("Hotel California", "Eagles", 5)
library["36"] = LibraryItem("Toxic", "Britney Spears", 4)
library["37"] = LibraryItem("Poker Face", "Lady Gaga", 4)
library["38"] = LibraryItem("Lose Yourself", "Eminem", 5)
library["39"] = LibraryItem("Anh Em Freestyle", "Wrxdie", 5)
library["40"] = LibraryItem("God's Plan", "Drake", 5)



def list_all():
    """Returns a formatted string of all tracks in the library."""
    track_list = []
    for key, track in library.items():
        track_list.append(f"{key}: {track.song} by {track.singer}, Rating: {track.rating}, Plays: {track.play_count}")
    return "\n".join(track_list)

def get_song(key):
    """Returns the song name for the given track key."""
    return library.get(key, None).song if key in library else None

def get_singer(key):
    """Returns the singer for the given track key."""
    return library.get(key, None).singer if key in library else None

def get_rating(key):
    """Returns the rating for the given track key."""
    return library.get(key, None).rating if key in library else None

def get_play_count(key):
    """Returns the play count for the given track key."""
    return library.get(key, None).play_count if key in library else None

def update_play_count(key, new_play_count):
    """Updates the play count for the track with the given key."""
    if key in library:
        library[key].play_count = new_play_count
    else:
        print(f"Track {key} not found.")

