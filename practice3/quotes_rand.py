import random
quotes=["No matter how handsome you are even baboons atract tourists",
        "When you wake up in the morning you always have two options to wake up and chase your dream or go back to bed and continue dreaming",
        "winning is never an option",
        "The future belongs to those who belive in the beauty of their dreams",
        "Your dreams are valid",
        "If you have a big butt then you are sitting on a gold mine",
        "You only live once"]
authors=["Allan",
         "Sam",
         "Meshack",
         "morgan",
         "wilson"]
def get(a,b):
    print("%s\n\t\t\t\t\t\tby %s"%(quotes[a],authors[b]))
for i in range(1):
    x=random.randint(0,len(quotes)-1)
    y=random.randint(0,len(authors)-1)
    get(x,y)
