import time
from Story import *
import os


def type_out_words(text, speed=0.02):
    """Prints text to the console as if it is being typed out, word by word."""
    # Split the text into lines and iterate through each line
    for line in text.strip().split('\n'):
        words = line.split()  # Split each line into words
        for word in words:  # Iterate through each word
            print(word, end=' ', flush=True)  # Print word with a space after it
            time.sleep(speed)  # Pause for a short duration
        print()


class Narrator:
    def __init__(self):
        # the user choices are stored for working out the story's final
        self.user_choice = []

        # below are all the story steps sorted out by step/branch
        self.introduction = [introduction,     # introduction
                             fork_in_the_road] # Step 1
        self.branch_A = [overgrown_path,       # Step 2A
                         monument,             # Step 3A1
                         living_grass]         # Step 3A2
        self.branch_B = [foggy_path,           # Step 2B
                         river_guardian,       # Step 3B1
                         unending_mist]        # Step 3B2
        self.final_decision = cabin_decision   # Final Decision
        self.endings = [safe_haven,               # ending 1
                        shadow_within,            # ending 2
                        river_gift,               # ending 3
                        lost_in_mist]             # ending 4
        # this starts the story
        self.flow_control_manager()

    # user input validation system
    def validate_input(self):
        user_choice = input()
        while user_choice not in ["A", "B"]:
            print('Invalid, please choose again:'"\n")
            user_choice = input()
        else:
            self.user_choice.append(user_choice)

    def print_ending(self):
        pass

    def flow_control_manager(self):
        type_out_words(self.introduction[0])
        type_out_words(self.introduction[1])
        self.validate_input()

        # step 1
        if self.user_choice[0] == "A":
            type_out_words(self.branch_A[0])
        elif self.user_choice[0] == "B":
            type_out_words(self.branch_B[0])
        self.validate_input()

        # step 2
        if self.user_choice[1] == "A":
            type_out_words(self.branch_A[1])


narrator = Narrator()

