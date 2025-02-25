# Advent of Code
### **My code written for "Advent of Code" 2024<br>**

[Advent of Code](adventofcode.com) is an Advent calendar of small programming puzzles for a variety of skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

I was motivated by our lecturer and wanted to beat the challenge 3 years later.
## Days 1 - 7
**Day 1** was self explainatory.<br>

**Day 2** I had a small problem with re-trying the reports without one of the levels, but wrote a function to test all cases.<br>

**Day 3** came with [regex](https://en.wikipedia.org/wiki/Regular_expression) problem. After a bit of research and tutorials of [re](https://docs.python.org/3/library/re.html) library in python, i completed part 1. Part 2 was tricky, but I am proud of my program. It divided corrupted memory into list of actions, that were later interpreted accordingly. <br>

**Day 4** was **hard**. I came up with an easy algorithm to set the input **string to a matrix** and then check words looking at "X"'s neighbours. The _hard part was coding it_. After a bit of help from ChatGPT I coded a checker in every dimension. Part 2 was surprising, but kind of easier. I checked for letters **"A"** in matrix and checked if words completed from diagonals matched the key: ```["MAS", "SAM"]```<br>

**Day 5** challenge was tricky, i quickly came up with my data structure - organizing things into lists _again_. Then for orders I checked for every order if update was correct. For part 2 I added searching for incorrect and a function to correct the orders.

**Day 6** I woke up at 6am to code in the morning. I liked the challenge because it reminded me of some **game mechanics**. I quickly made the data structure thanks to experience from earlier days. Hard part was simulating part 2. I had to optimize the trying algorithm, because first version took too long to calculate. It also reminded me of [halting problem](https://en.m.wikipedia.org/wiki/Halting_problem). It took me 2 hours to complete.

**Day 7** //TODO<br>

## Days 8 - 15

**Day 8** //TODO<br>

**Day 9** The problem seemed to be easy, today I learned something about printing lists easier with ```print(''.join(list))```. Part 2 i got the example but the input didnt work for me. The principle seemed to be easier than it was.<br>

**Day 10** It seemed as an easy problem. I found bases (zeros) and then I looked up that a ```Depth First Search``` algorithm can solve it. The rest was implementing it. Distinct paths were very hard, but seemed managable.<br>

**Day 11** Part 1 was really easy, at 6:50AM i got the answer. Part 2 required recursion and memoization, because the first one was about ```O(2^k*n)``` complexity. so a lot. 

**Day 12** Map of fields, very hard problem. ;c

**Day 13** Was a fun math challenge. I used diofantine equiation. Part 1 took me a half of lecture and part2 didnt work right away.

**Day 14** I am very happy with my code. First, I wrote an algorithm on paper to know what functions I need to have, and then just coded them, *(and it worked!!!)*. I worked with lists as data structure again, but in a different way. Instead of making a list visually, i had:
```positions``` ```velocities``` ```quadrants``` Each list was synchronized with indexes, so robot's data was in ```pos[i] vel[i] quad[i]```. Looking for tree i solved with looking if every robot is in distinct location, and then print the map and seconds it took.

**Day 15** Another day with robots! My concept for today was very simple, but parsing the input and logic of moving multiple boxes took me a long long time. My gps counter worked good on test, but didnt work on input, or it was the moving, idk really.

## Days 15 - 25

Didn't write updates on them daily ;cc
...
<br>

**_score: 50/50 stars <br>
class leaderboard position: #13/46_**



