"""Copyright (c) 2017 * Keith Cestaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


intro = "You wake up on the ground in a strange place. It's dark, but \
you see light coming from an opening to your left. (possible options: \
walk left, look around more)"

inventory = []
health = 100

pOption = ""


def checkDefaultOptions(pOption):
    if pOption == "/inventory":
        print(inventory)
    elif pOption == "/health":
        print(str(health))
    else:
        print("input a valid action")

print(intro)
print()
while pOption != "walk left":
    pOption = str(input())
    if pOption == "walk left":
        print("You slowly get up and walk down a corridor. While walking \
you discover a sword. Do you pick it up? (possible options: yes, no)")
    elif pOption == "look around more":
        print("You look closer at your surroundings and realize that you're in \
a cave of some sort. You have nothing on you but your clothes. (possible \
options: walk left)")
    else:
        checkDefaultOptions(pOption)
    print()

while pOption != "yes" and pOption != "no":
    pOption = str(input())
    if pOption == "yes":
        print("You go to pick up the sword and put it in your inventory.")
        inventory.append("Sword")
    elif pOption == "no":
        print("You walk around the sword.")
    else:
        checkDefaultOptions(pOption)
    print()

print("You continue walking down the corridor until you reach what seems to be \
a dead end. On further analysis you realize that you are standing in front of \
what appears to be a locked door. (possible actions: shove open, look for \
key, examine door, throw rock at it)'")

while (pOption != "examine door"):
    pOption = str(input())
    if pOption == "shove open":
        print("You try shoving the door but it won\'t budge.")
    elif pOption == "look for key":
        print("You look around for a key but don\'t see anything.")
    elif pOption == "examine door":
        print("You examine the door further and realize there is a knob. \
How did you miss that eartlier? You turn the knob and the door opens. That was \
easier than you were expecting.")
    elif pOption == "throw rock at it":
        print("You throw a rock at the door and it bounces back and hits \
you. You realize what a silly decision that was.")
    elif pOption == "/inventory":
        print(inventory)
    else:
        checkDefaultOptions(pOption)
    print()