import time
from Story import *
import os

def type_out_words(text, speed=0.1):
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
        self.user_choice = []
        self.story_steps = [introduction,         # introduction
                            fork_in_the_road,     # Step 1
                            overgrown_path,       # Step 2A
                            foggy_path,           # Step 2B
                            monument,             # Step 3A1
                            living_grass,         # Step 3A2
                            river_guardian,       # Step 3B1
                            unending_mist,        # Step 3B2
                            cabin_decision]       # Final Decision
        self.endings = [safe_haven,               # ending 1
                        shadow_within,            # ending 2
                        river_gift,               # ending 3
                        lost_in_mist]             # ending 4
        self.flow_control_manager()

    # user input validation system
    def validate_input(self):
        user_choice = input()
        if user_choice in ["A", "B"]:
            self.user_choice.append(user_choice)
            os.system('cls' if os.name == 'nt' else 'clear')  # if input is validated, console is cleared for next step
            return True
        else:
            return False, "Invalid input, please choose again."

    # the relevant user choices are appended for final ending calculation
    def append_choice(self, user_choice):
        self.user_choice.append(user_choice)
        return self.user_choice

    def print_ending(self):
        pass

    def flow_control_manager(self):
        type_out_words(self.story_steps[0])
        type_out_words(self.story_steps[1])


narrator = Narrator()

