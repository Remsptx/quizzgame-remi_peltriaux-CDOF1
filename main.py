# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:33:24 2024

@author: rempt
"""

import random
from fuzzywuzzy import fuzz


class Quiz:
    def __init__(self, questions_dict,mcq):
        self.questions_dict = questions_dict
        self.mcq = MCQ_Question

    def askMcq(self):
        i = 1
        print(self.mcq["question"])
        for possibilitie in self.mcq["possibilities"] : 
            print(f"{i} : {possibilitie}")
            i+=1
        answer = int(input("Who's your answer ? (use the numbers) : "))
        if answer == self.mcq["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is :", self.mcq["possibilities"][self.mcq["answer"]-1])

    def ask(self):
        random_question = random.choice(list(self.questions_dict.keys()))
        correct_answer = self.questions_dict[random_question]

        user_answer = input(random_question + "\n")
        score = fuzz.ratio(user_answer.lower(), correct_answer.lower())
        if score > 80:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

history_questions = {
    "1. Who was the first President of the United States?": "George Washington",
    "2. In which year did Christopher Columbus first reach the Americas?": "1492",
    "3. What was the name of the ship that brought the Pilgrims to America in 1620?": "Mayflower",
    "4. Who was the primary author of the Declaration of Independence?": "Thomas Jefferson",
    "5. What was the name of the ship that carried the Pilgrims to Plymouth Rock?": "Mayflower",
    "6. In what year did the Titanic sink?": "1912",
    "7. Which famous explorer circumnavigated the globe in the 16th century?": "Ferdinand Magellan",
    "8. What ancient city was known for the Hanging Gardens?": "Babylon",
    "9. Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "10. What was the main cause of the Great Depression in the 1930s?": "Stock market crash of 1929",
    "11. Who was the leader of the Mongol Empire in the 13th century?": "Genghis Khan",
    "12. Who was the first woman to fly solo across the Atlantic Ocean?": "Amelia Earhart",
}

MCQ_Question = {
    "question" : "What's the impostor among the new 7 Wonders of the World ?",
    "possibilities" : ["Great Wall of China","Alexandria Lighthouse","The Machu Pichu"],
    "answer" : 2
} 


history_quiz = Quiz(history_questions,MCQ_Question)
history_quiz.askMcq()

nb_questions = int(input("How many questions? "))
i = 0

while i < nb_questions:
    history_quiz.ask()
    i += 1

