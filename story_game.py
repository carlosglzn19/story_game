print('''    *                             |>>>                    +
+          *                      |                   *       +
                    |>>>      _  _|_  _   *     |>>>
           *        |        |;| |;| |;|        |                 *
     +          _  _|_  _    \\.    .  /    _  _|_  _       +
 *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
               \\..      /    ||:+++. |    \\.    .  /           *
      +         \\.  ,  /     ||:+++  |     \\:  .  /
                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
                 ||+++ ||.    .     .      . ||+++.|   *
+   *            ||: . ||:.     . .   .  ,   ||:   |               *
         *       ||:   ||:  ,     +       .  ||: , |      +
  *              ||:   ||:.     +++++      . ||:   |         *
     +           ||:   ||.     +++++++  .    ||: . |    +
           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
                 ||: . ||: ,   +++++++ .  .  ||:   |        *
                 ||: . ||: ,   +++++++ .  .  ||:   |''')
print("Welcome to the treasure castle!")
print("Your mission is to find the treasure")

first_step = input('You enter the hall of the castle. Which way do yo go? "left" or "right")\n')
if first_step.lower() == "left":
    second_step = input('You see the kitchen and the art room. Where do you go? Type "kitchen" or "art".\n')
    if second_step.lower() == "art":
       last_step = input('You encounter three doors: one yellow, one green and one blue. Which door do you open? Type "yellow", "green" or "blue".\n')
       if last_step.lower() == "blue":
           print("Congratulations!! You found the treasure. You are rich now!!")
       else:
           print("Game over! You were eaten by a lion!")
    else:
        print("Game over! A monster caught you!")
else:
    print("Game over! You fell into a trap!")
    

