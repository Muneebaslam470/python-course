import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute ('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,   
               time TEXT NOT NULL         
    )
''')

def list_videos():
    print("\n")
    print("*" * 70)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES( ?,?)",(name, time)) 
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?" , (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager with DB, Choose your choice : ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. delete a youtube video ")
        print("5. Exit the App ")
        choice = input("Enter your choice here : ")

        if choice == '1':
            list_videos()
        elif choice == "2":
            name = input("Enter your name : ")
            time = input("Enter your time : ") 
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter your video ID here for update : ")
            name = input("Enter your name : ")
            time = input("Enter your time : ") 
            update_video(video_id, name , time)
        elif choice == "4":
            video_id = input("Enter your video ID to delete : ")
            delete_video(video_id)                       
        elif choice == "5":
            break
        else:
            print("Invalid choice !") 

    conn.close()
        
if __name__ == "__main__":
    main()