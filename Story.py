introduction = """
You wake up in a dense, magical forest. The trees tower above, their branches tangled in webs of mist. The air is thick with damp earth and mysterious sounds that make your heart race.
"""

# Step 1
fork_in_the_road = """
After wandering for a short while, you come across a fork in the road. The paths seem to be calling to you in different ways.
A) A narrow path, overgrown with thorny bushes and leading into a darker section of the forest.
B) A wide, well-trodden path, shrouded in a dense fog that makes it impossible to see far ahead.
"""

# Step 2A (Overgrown Path)
# Triggered if user chooses A in step 1
overgrown_path = """
Pushing through the thorny bushes, you find yourself in a small clearing. In the center stands a strange stone monument, its surface covered in cryptic symbols. It pulses with an eerie energy.
A) Approach the monument and try to read the symbols.
B) Stay back, observing it from a distance.
"""

# Step 2B (Foggy Path)
# Triggered if user chooses  B in step 1
foggy_path = """
The fog thickens as you continue down the wide path. Soon, you can barely see your hands in front of you. Suddenly, you hear the sound of rushing water nearby, cutting through the mist.
A) Investigate the source of the water.
B) Continue walking, trusting the path to lead you out of the fog.
"""

# Step 3A1 (Monument)
# triggered if users chooses A in step 2A
monument = """
As you touch the monument, the ground beneath you rumbles and a hidden door opens. A spiral staircase descends into the earth, beckoning you into darkness.
A) Descend the stairs and explore the underground.
B) Step back and stay in the clearing, unsure of what lies below.
"""

# Step 3A2 (Living Grass)
# triggered if users chooses B in step 2A
living_grass = """ 
You stay at the edge of the clearing, but suddenly the grass begins to move as though it’s alive. It wraps around your feet, pulling you down toward the earth.
A) Struggle against the grass, pulling yourself free.
B) Relax and let the grass take you, curious about where it will lead.
"""

# Step 3B1 (River Guardian)
# Triggered if user chooses A in step 2B
river_guardian = """
You follow the sound of rushing water and find a glistening river flowing through the fog. As you approach, a figure rises from the water—part human, part river—watching you silently.
A) Speak to the river guardian and ask for guidance.
B) Step back, afraid of what it might want, and leave the river behind.
"""

# Step 3B3 (Unending Mist)
# Triggered if user chooses b in step 2B
unending_mist = """
You press forward through the thickening fog. Suddenly, you can’t see anything at all. No sound, no light, only mist. You feel as if the world is shrinking around you.
A) Call out for help, hoping someone will hear you.
B) Remain silent, trusting your instincts to guide you out.
"""

# Final Decision at the Cabin
cabin_decision = """
After many twists and turns, you come across an old, abandoned cabin deep in the woods. Smoke rises from its chimney, though it appears deserted. Exhausted and cold, you face a final decision.
A) Enter the cabin, hoping to find shelter and food inside.
B) Stay outside, wary of what might be lurking within.
"""

# Endings

# Ending 1
# Triggered if user came down the Overgrown path and chooses A
safe_haven = """
You step cautiously inside the cabin. To your surprise, the interior is warm and welcoming. A fire crackles in the hearth, and food is laid out on a table as if waiting for you. Exhausted, you sit by the fire, grateful to have found a safe place. You rest here peacefully, having finally escaped the forest’s dangers.
"""

# Ending 2
# Triggered if user came down the Overgrown path and chooses B
shadow_within = """
You decide to stay outside, unwilling to trust the seemingly peaceful cabin. As night falls, the forest grows colder and darker. The shadows of the forest close in, and you realize you’ve been lured into its depths. The darkness swallows you whole, and you become just another lost soul in the Forest of Many Paths.
"""

# Ending 3
# Triggered if user came down the Foggy path and chooses A
river_gift = """
You step into the cabin, and as soon as the door closes behind you, the fog that had surrounded you begins to clear. Inside, a figure you recognize—part human, part river—stands by the fire, offering you rest and protection. You have escaped the fog’s grip, safe at last.
"""

# Ending 4
# Triggered if user came down the Foggy path and chooses B
lost_in_mist = """
You choose to stay outside, hoping to avoid whatever strange forces inhabit the cabin. The fog thickens around you, and soon you can barely see. No matter which direction you turn, the mist deepens. You realize you are forever trapped in the endless fog, wandering without escape.
"""