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
print(intro)
print()
playerOption = str(input())
if playerOption == "walk left":
    print("You slowly get up and walk down a corridor. While walking \
you discover a sword. Do you pick it up? (possible options: yes, no)")
    print()
    playerOption = str(input())
elif playerOption == "look around more":
    print("You look closer at your surroundings and realize that you're in \
a cave of some sort. You have nothing on you but your clothes. (possible \
options: walk left)")
    print()
    playerOption = str(input())
    if playerOption == "walk left":
        print("You slowly get up and walk down a corridor. While walking \
you discover a sword. Do you pick it up? (possible options: yes, no)")
        print()
        playerOption = str(input())
    else:
        print("input a valid action")
        print()
else:
    print("input a valid action")
    print()