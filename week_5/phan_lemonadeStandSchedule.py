"""
Author: Christopher Phan
Date: 2/15/26
File Name: phan_lemonadeStandSchedule.py
Description: Schedule for lemonade stand
"""

lmStandToDoList = ["Squeeze Lemons", "Buy Sugar", "Clean Jugs and prepare cups", "Set up Stand", "Mix lemon juice and sugar in the jugs"]

for task in lmStandToDoList:
  print(task)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day, task in zip(days, lmStandToDoList):
  if day == "Saturday" or day == "Sunday":
    print(f"{day}: It is a day off. It is important to rest.")
  else:
    print(f"{day}: Your task is to {task}.")