# DinosaurHandSimulator
A Script to generate sample hands and test for available combos

Notes: The algorithm is very dumb and greedy and will prioritize picking Giant Rex from Pot of Prosperity over good Hand Traps, just to make Dolkka earlier.

In general: The algorithm always uses Pot of Prosperity and then uses all the Fossil Digs it has. At each of these junctures it will try all available options.

As a matter of principle the script tries to meticulously verify whether all requirements for a combo are indeed met (so it is not fooled by stupid deck building like 0 Miscs). The exceptions occur due to laziness and are noted in comments.
