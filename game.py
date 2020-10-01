from random import randint


def short_game():
    print("WELCOME TO THIS SHORT GAME")
    name = input("what's your name ")
    age = int(input("What's your age? "))
    print(f"Welcome {name}")

    if age in range(0, 17):
      print("Come back when you're 18")
      age += 1
      exit
    else:
      print("Viollla!!! LET'S PLAY SOME GAMES")

      subject = input("Chose a Subject English/Math ").lower()
      if subject == "english":
        print("Let's move")
        choice = input("What do you prefer,\n poetry/RPS(rock,paper, scissors) ").lower()
        if choice == "poetry":
          print("9LIVES \n\nTo the boy on the street \nWaging war from within \nTo the girl who refuses \nTo be someone who he abuses \nI offer you nine lives.\n\nby Ibraheem Uthman")
          exit
        else:
          t = ["Rock", "Paper", "Scissors"]
          computer = t[randint(0,2)]
          player = False

          while player == False:

            player = input("Rock, Paper, Scissors?").lower()
            if player == computer:
              print("TIE!!!")
            elif player == "rock":
                if computer == "paper":
                  print("You lose!", computer, "covers", player)
                else:
                  print("You win!", player, "smashes", computer)
            elif player == "paper":
                if computer == "scissors":
                   print("You lose!", computer, "cuts", player)
                else:   
                   print("You win!", player, "covers", computer)  
            elif player == "scissors":
                if computer == "rock":
                  print("You lose!", computer, "smashes", player)
                else:
                  print("You win", player, "cuts", computer)
            else:
                print("That's not a valid play, check your spelling")

            player = False

            computer = t[randint(0,2)]    
                 


          exit
      else:
        print("Let's do this, Mathematician")
        topic = input("What topic do you prefer? fibonacci/AreaOfaTriangle ").lower()
        if topic == "fibonacci":
          exec
        def fib(n):
            n = int(input("Put in a number "))
            if n < 1:
                 return None
            if n < 3:
                return 1

            elem1 = elem2 = 1
            sum = 0
            for i in range(3, n + 1):
                sum = elem1 + elem2
                elem1, elem2 = elem2, sum
            return sum

        for n in range(1, 10):
            print("The fibonacci is --> ", fib(n))
            break
        else:
          exec
          def heron(a, b, c):
             a = float(input("Your fist agnle "))
             b = float(input("Your second angle "))
             c = float(input("Your third angle "))
             p = (a + b + c) / 2
             return (p * (p - a) * (p - b) * (p - c)) ** 0.5
          print(heron(a,b,c))
short_game()
print("Copyright: Ibraheem Uthman")
