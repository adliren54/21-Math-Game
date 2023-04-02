print("Math Game!")

multiples = int(input("Name your multiples: "))
score = 0

for i in range(1, 11):
  print(i, "x", multiples, "=")
  predict = int(input("What is your anwer? "))
  answer = i * multiples
  if predict == answer:
    score += 1
    print(score)
    print("Great work!")
  else:
    print("Nope! The answer was", answer)

if score == 10:
  print("Wow! That's a perfect score 🥳")
elif score < 10:
  print("You scored", score, "out of 10!")