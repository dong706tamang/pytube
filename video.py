from pytube import YouTube 

def progressComplete(stream,file_path):
    print("Download Complete")

link=input("enter your video link from youtube :")

link=link.split(",")

for i in link:
    i = i.strip()

    vid=YouTube(i)

    mp4files = vid.streams.filter(file_extension="mp4",progressive=True).order_by("resolution")

    print(f"\n[+]{vid.streams[0].title}\n")

    vid.register_on_complete_callback(progressComplete)

    if len(link) == 1:
        for i in range(len(mp4files)):
           print(f"{i}. {mp4files[i].resolution}")

        res = int(input("\nSpecify Resolution:-"))
        res = mp4files[res].resolution
        mp4files.filter(resolution=res).order_by("resolution").last().download()

    else:
        mp4files.last().download()