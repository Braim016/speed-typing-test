# import all required modules
from tkinter import *
import time
import difflib
import re
from random import *

# Declaring the global variables that will be used inside functions' scopes
global start_time
global end_time


# Function to split words
def tokenize(s):
    return re.split('\s+', s)


# Function to join words
def untokenize(ts):
    return ' '.join(ts)


# Function to check if two words are equal
def equalize(s1, s2):
    # Splitting the teo inputs into words
    l1 = tokenize(s1)
    l2 = tokenize(s2)
    # Creating an empty list to put the words into for comparison
    res1 = []
    res2 = []
    # Creating a variable to check for a match
    prev = difflib.Match(0, 0, 0)
    # Iterating over the words to check where a word doesn't match the word from the two inputs
    for match in difflib.SequenceMatcher(a=l1, b=l2).get_matching_blocks():
        # Checking if there is a word that is in sentence 1 that doesn't match sentence 2 and vice versa
        # Then adding a '_' if there is a mismatch
        if prev.a + prev.size != match.a:
            for i in range(prev.a + prev.size, match.a):
                res2 += ['_']
            res1 += l1[prev.a + prev.size:match.a]
        if prev.b + prev.size != match.b:
            for i in range(prev.b + prev.size, match.b):
                res1 += ['_']
            res2 += l2[prev.b + prev.size:match.b]
        # Returning the words to lists
        res1 += l1[match.a:match.a + match.size]
        res2 += l2[match.b:match.b + match.size]
        prev = match
    # Returning the words as a sentence
    return untokenize(res1), untokenize(res2)


# Creating the root tkinter window
root = Tk()
root.title("Speed Typing Test")
# root.iconbitmap('C:\\Users\\HP_ELITE\\Documents\\favicon.ico')

# Creating and griding the entry widget
e = Entry(root, width=150, borderwidth=5, font=('Helvetica', 12))
e.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Creating a function for the start button
def start_test():
    global start_time
    # Starting the counter
    start_time = time.perf_counter()
    # Displaying the text on the screen
    start_label = Label(root, text=sample_list[n], font=('Helvetica', 9))
    start_label.grid(row=3, column=0, columnspan=2)


# Creating a function for the end button
def end_test():
    global end_time
    # Stopping the counter
    end_time = time.perf_counter()
    # Display a text to show that the exercise is done
    end_label = Label(root, text="You have successfully completed the typing test. Your result is as follows:",
                      font=('Helvetica', 12))
    end_label.grid(row=5, column=0, columnspan=2)
    # Calculating the time taken
    time_taken = end_time - start_time
    # Time taken in minutes
    min_time = time_taken / 60
    # Setting the sample text and what was entered into the entry widget to the s1 and s2 variables from the equalize
    # function
    s1 = sample_list[n]
    s2 = e.get()
    # Using the equalize function and setting to a variable
    x = equalize(s1, s2)
    # Finding the gross and net wpm along with the accuracy
    gross_wpm = (len(s2) / 5) / min_time
    net_wpm = ((len(s2) / 5) - x[1].count("_")) / min_time
    accuracy = net_wpm / gross_wpm * 100
    # Rounding the gross and net wpm to the nearest whole integer
    gross_wpm = int(gross_wpm)
    net_wpm = int(net_wpm)
    # Rounding the accuracy to the nearest 2 decimal place
    accuracy = round(accuracy, 2)
    # Creating the result text
    result_text = f"GROSS WPM: {gross_wpm} WPM \nNET WPM: {net_wpm} WPM \nACCURACY: {accuracy}%"
    result_label = Label(root, text=result_text, font=('Helvetica', 12))
    result_label.grid(row=6, column=0, columnspan=2)
    # Printing the first result to know how correct the program is
    # print(x[1])
    # Clearing the entry widget
    e.delete(0, END)


# Sample texts
sample_text1 = 'The silence shuffles. His heart leaps to his throat. He dares not turn, lest the package rustle, ' \
               'but he twists his eyeballs till they hurt and there stands Big Sister. Heart slides back to his toes, ' \
               'eyes squeezing shut, never to see the manicured hand also creeping for a taffy. Marigold Packwood is ' \
               'just a plain girl. '
sample_text2 = 'Only after he died did I find the mask. The cracked, clay façade my father put on every day. Put on ' \
               'to appease the world. To earn their mercy. Their bigoted praise. But how broken he was underneath. ' \
               'Weeping to be loved, given justice for who he had always been. '
sample_text3 = 'How fast the clock’s hands run to the finish line of my motherland’s life. How innocently my ' \
               'belongings gaze back at me, like orphans, begging me: “Please, pick me.” My suitcases, ' \
               'these memorable treasures, have become the smallest bags in the world. Why won’t all of me fit into ' \
               'them? '
sample_text4 = 'It’s a habit: looking out my kitchen window. Checking to see if my neighbor’s car is parked. Relief ' \
               'when I see it, Knowing he’s safe. Irene never returned from the trip to PA for her chemo treatments. ' \
               'Hit a tree. Took days to discover. Broke in to rescue her dog. '
sample_text5 = 'I browsed the rack of photos and flicked through the plastic wallets for something suitable. Perhaps ' \
               'a meaningful word this time? The end of a relationship should be marked in some way. “See anything ' \
               'you like?” he asked. I caught his eye—bright blue, long, dark lashes. “Not today, thanks.” '
sample_text6 = '“Hey, idiot!” boomed the voice from the kitchen. It bombarded Mary with disparaging remarks. She felt ' \
               'trapped, insecure. A rotten stench arose with each insult. Fed up, Mary stormed the kitchen, ' \
               'tore off the lid, and took out the trash. She kept walking, free and refreshed. She didn’t turn back. '
sample_text7 = 'At your age I cherished the Magic Hour—the rotund warmth of widening day, kneeling before the ' \
               'advance, ah! of night, caravan clouds towing it aloft in a shush of cool air the trees exhaled in ' \
               'unison.” He paused, teary. “I’m sorry you will never know that swell of sweetness.” '
sample_text8 = 'Without believing, I let out prayers like popcorn begging for angels to be real. After the darkness ' \
               'and the quiet, small stones of ceiling plaster continue to fall teeth from heaven. I am covered. The ' \
               'roof and floor groan for me. My prayers are softer now, each one a surprise. '
sample_text9 = 'There was no more honey. She drove to the store, independently. Parked and shuffled in. There, ' \
               'on the bottom shelf. The weight of gold, too heavy. The check-out, too far away. Impossible, ' \
               'she realized. She turned and left. Tap-tapping with her cane to the car. Then home, to bitter tea. '
sample_text10 = "Gathering from given were us moveth you. Whose doesn't can't grass us third don't. Brought male kind " \
                "waters god. Thing beast yielding kind. Shall was meat night he so. Gathering have, saw which also " \
                "subdue under firmament fourth divide. Firmament female lesser, life won't. Make third won't under " \
                "was open. "
sample_text11 = "God gathering divided beast subdue over hath. Us night fish. Whose cattle Doesn't fruit said That " \
                "you night lesser him creature is third all Stars gathering lights under yielding dominion void " \
                "creature without multiply, fifth male. First. Them given don't one sea evening you'll kind wherein " \
                "living all every give. "
sample_text12 = "Image second his rule let Thing. You. Appear dominion divided form. Deep seed be. They're itself. " \
                "Their forth gathered herb life after bring fill god fish fifth moved make darkness whose fruitful. " \
                "Deep also. Evening seasons. Abundantly beast be to shall, won't image you, that fowl. In fill. Was. " \
                "Lights. "
sample_text13 = 'Whales moveth all which years the hath were moved dry fowl that male saying, every, them him moved ' \
                'give second beast set signs sea kind good him winged their divide and. Beginning together fruit void ' \
                'for there night upon second fowl which firmament cattle. So own fish For yielding female. '
sample_text14 = 'Unto sixth third in day earth Forth female that, two beginning let, of from morning life face second ' \
                'male own seas beast whose earth Fowl their there whales created. God thing which let hath in a let ' \
                'one cattle rule after rule winged were own and beginning to after. Them. '
sample_text15 = "Form heaven Was, divided him bring lesser earth fruitful hath without fowl one replenish above " \
                "waters replenish greater won't image they're yielding likeness greater form, good. Have fruit waters " \
                "let to form wherein be meat the very shall great waters fourth seasons together replenish. "

# Picking a random text from 1 to 15
n = randint(0, 15)

# The list of sample texts
sample_list = [sample_text1, sample_text2, sample_text3, sample_text4, sample_text5, sample_text6, sample_text7,
               sample_text8, sample_text9, sample_text10, sample_text11, sample_text12, sample_text13, sample_text14,
               sample_text15]

# Displaying heading text
heading = Label(root, text="SPEED TYPING TEST", font=('Helvetica', 32, 'bold'))
heading.grid(row=0, column=0, columnspan=2)

# Displaying the instructions text
instructions = Label(root,
                     text="Welcome to my Typing Test. Once you click on 'Start Typing', the text you're to type will "
                          "show up "
                          "and whenever you're done typing, kindly click End Test \n Make sure you maximize the "
                          "screen before you start. Good luck!", font=('Helvetica', 12))
instructions.grid(row=1, column=0, columnspan=2)

# Start button
start_button = Button(root, text="Start Typing", padx=40, pady=20, command=start_test, font=('Helvetica', 12))
start_button.grid(row=4, column=0)

# End button
end_test = Button(root, text="End Test", padx=40, pady=20, command=end_test, font=('Helvetica', 12))
end_test.grid(row=4, column=1)

root.mainloop()
