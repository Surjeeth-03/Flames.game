import time
import sys

lyrics = [
 "P O O J I T H A",
 " P O O J I T H",
   "  P O O J I T",
    "   P O O J I",
     "    P O O J",
      "     P O O",
       "      P O",
        "       P"
]

def type_line(line, delay=0.07 ):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def animate_lyrics(lines):
    for line in lines:
        type_line(line)
        time.sleep(0.3)


if __name__== "__main__":
    animate_lyrics(lyrics)