import random

# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
        

# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self, data):
        self.start_node = None
        self.data = data
        self.next = None
        self.head = None
        self.tail = None
        self.previous = None

    def size(self):
        self.length = 0
        return self.length

    # Insert items to list
    def add(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    def delete(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return
             
        if index == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return
         
        start = self.head
        for i in range(index):
            start = start.next
        start.previous.next, start.next.previous = start.next, start.previous
        self.count -= 1
        return
        
    def topSong(self):
        return self.head.data

    # Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Song: ", n.item)
                n = n.next
        print("\n")
   
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))

    def __repr__(self):
        return "%s %s" % (self.title, self.artist)
        
    
class songViewer():
    def __init__(self,data):
        self.songlist = doublyLinkedList(data)
        self.currentSong = None

    def add(self,songTitle, songArtist):
        newSong = Song(songTitle, songArtist)
        self.songlist.add(newSong)
    
    def view(self, Song = None):
        if Song:
            self.currentSong = Song
        if not self.currentSong:
            self.currentSong = self.songlist.Display()

    def remove(self, index) -> int:
        if(index < 0 ) or (index > self.songlist.size()-1):
            return 0
        self.songlist.delete(index)
        return True
    
    def skip(self):
        self.currentSong = self.currentSong.next

        if not self.currentSong:
            self.currentSong = self.songlist.Display()

        self.view(self.currentSong)

    def rewind(self):
        self.currentSong = self.currentSong.prev
        if not self.currentSong:
            self.currentSong = self.songlist.getEnd()
        self.view(self.currentSong)

    def topSong(self):
        self.currentSong = self.songlist.topSong()
    
    def showCurrentSong(self):
        if self.currentSong:
            print(self.currentSong.data)
        else:
            print("No Song currently being played.")
    
    def shuffle(self):
        random.shuffle(self.songlist)

# Insert the element to the list
mySongViewer = songViewer(data=None)
mySongViewer.add("End of the Road","test")
mySongViewer.add("Old Town Road","test")
mySongViewer.add("Song4","test")
mySongViewer.add("Song5","test")
mySongViewer.add("Song6","test")

print()
def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        song = input("Please enter Song Title to add: ")
        artist = input("Please enter Song Artist to add: ")
        mySongViewer.add(song,artist)
        # Add song to playlist
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        value = int((input("Please enter Song number you would like to remove: ")))
        mySongViewer.remove(value)
        print("Song "+str(value)+" Removed to Playlist")

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        songPlaying = mySongViewer.topSong()
        print("Playing "+songPlaying+"...")        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        mySongViewer.skip()                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        mySongViewer.rewind()  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
        mySongViewer.shuffle()
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ") 
        mySongViewer.showCurrentSong()   
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        mySongViewer.view()
    elif choice == 0:
        print("Goodbye.")
        break

            
