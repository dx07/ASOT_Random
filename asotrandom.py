import os
import random
import webbrowser

HISTORYFILE = "history.log"
MAX_EPISODE = 800

def get_episode_name(id):
    return (("in-2-trance-" if id in range(1,4) else "a-state-of-trance-")+str(id)) if id > 0 else "into-trance" if id == -4 else "into-trance-"+str(id+5)

while (True):

    if os.path.isfile(HISTORYFILE):
        with open(HISTORYFILE, 'r') as h:
            history = [int(line.replace('\n','')) for line in h.readlines()]
        last = history[-1] if len(history)>0 else None
    else:
        history = []
        last = None

    print                 ("****** ASOT Random Episode ******\n")
    if last != None: print(" (Enter) Last Episode: "+str(last))
    print                 (" (0)     New Random Episode")
    if last != None: print(" (1)     Reset Previous Episode")
    print                 (" (2)     Quit")
    choice = input("\nYour choice... ")

    if choice == "" and last != None:
        webbrowser.open("http://asotarchive.org/episode/"+get_episode_name(last))
        break

    elif choice=="0":
        
        episodes = [e for e in list(range(-4,MAX_EPISODE+1)) if e not in history]
        new = random.choice(episodes)

        with open("history.txt", 'a') as h:
            h.write(str(new)+"\n")

        webbrowser.open("http://asotarchive.org/episode/"+get_episode_name(new))
        break

    elif choice=="1" and last != None:
            
        choice = input("\nEpisode "+str(last)+" will be put back in the list, continue? (y|n) ")
        
        if (choice == "y"):
            with open("history.txt", 'r') as h:
                content = h.readlines()[:-1]

            with open("history.txt", 'w') as h:
                h.writelines(content)

        print()
    
    else:
        break

