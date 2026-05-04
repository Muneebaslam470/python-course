import json ,os

def load_data():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, 'youtube.txt')
       
        with open( file_path, 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, 'youtube.txt')

    with open( file_path, 'w') as file:
        json.dump(videos , file)        

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index , video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input("Enter video name :")
    time = input("Enter video time :")
    videos.append({'name':name, 'time':time })
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update :"))
    if 1 <= index <= len(videos):
        name = input("Enter the video name :")
        time = input("Enter the video time :")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to delete :"))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid index selected")




def main():

    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose your choice ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter your choice :")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)        
            case "4":
                delete_video(videos)    
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()