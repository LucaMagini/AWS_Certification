import os, json, random
from termcolor import colored

os.system('color')

with open('AWS_Services.json') as file:
    aws_test = file.read()
aws_test = json.loads(aws_test)

num_quest = aws_test["Config"]["Number of Questions"]
        

while True:

    print("\n----- " + aws_test["Config"]["Title"] + " -----\n\n")
    print("1 -- " + aws_test["Config"]["Topics"][0] + " \n2 -- " + aws_test["Config"]["Topics"][1])

    num = input("\nChoose an option: ")
    while num not in ["1", "2"]:
        num = input(("Select a valid option: "))
    
    try:
        if int(num) == 1:
             
            services = aws_test["AWS Services"]  
            questions = list(services.keys())
            answers = list(services.values())
            print("\n\n--- " + aws_test["Config"]["Topics"][0].upper() + " ---\n\n")
            
            score = 0
            for n in range(num_quest):
                quest = random.choice(questions)
                questions.remove(quest)
                answ = [services[quest]]
                while len(answ) < 4:
                    elem = random.choice(answers)
                    if elem not in answ:
                        answ.append(elem)       
                random.shuffle(answ)
                print("{}. {}\n\nA - {}\nB - {}\nC - {}\nD - {}\n".format(n+1, quest, answ[0], answ[1], answ[2], answ[3]))
                choice = input("\nYour choice: ")
                while choice not in ["A", "B", "C", "D"]:
                    choice = input(("Select a valid option: "))
                
                if services[quest] is answ[ord(choice) - 65]:
                    score += 1
                    print(colored("CORRECT\n", "green"))
                else:
                    print(colored("WRONG\n", "red"))
                     
            if score / num_quest < 0.75:        
                print("\nYour score is:", colored("{}/{}".format(score, num_quest), "red"), "\n\n")
                
            else:
                print("\nYour score is:", colored("{}/{}".format(score, num_quest), "green"), "\n\n")
                
        elif int(num) == 2:
            
            print("\n\n--- " + aws_test["Config"]["Topics"][1].upper() + " ---\n\n")
            topics = list(aws_test["Other Questions"].keys())
            score = 0
            quest_list = {}
            
            for elem in topics:
                quest_list[elem] = list(aws_test["Other Questions"][elem].keys())
            for n in range(num_quest):
                
                # topic = random.choice(topics)
                # questions = list(aws_test["Other Questions"][topic].keys())
                # answers = list(aws_test["Other Questions"][topic].values())
                # quest = random.choice(questions)
                topic = random.choice(list(quest_list.keys()))
                print(topic)
                questions = quest_list[topic]
                answers = list(aws_test["Other Questions"][topic].values())
                quest = random.choice(questions)
                quest_list[topic].remove(quest)
                if len(quest_list[topic]) == 0:
                    quest_list.pop(topic, None)
                
                print("\n{}.".format(n+1), quest, "\n")
                random.shuffle(answers)
                possible_answ = []
                for count, elem in enumerate(answers):
                    print("{} - {}".format(chr(count + 65), elem))
                    possible_answ.append(chr(count + 65))
                    
                    
                choice = input("\nYour choice: ")
                while choice not in possible_answ:
                    choice = input(("Select a valid option: "))
                
                if aws_test["Other Questions"][topic][quest] is answers[ord(choice) - 65]:
                    score += 1
                    print(colored("CORRECT\n", "green"))
                else:
                    print(colored("WRONG\n", "red"))
                     
            if score / num_quest < 0.75:        
                print("\nYour score is:", colored("{}/{}".format(score, num_quest), "red"), "\n\n")
            else:
                print("\nYour score is:", colored("{}/{}".format(score, num_quest), "green"), "\n\n")
        else:
            print("*** Please choose a valid option ***")            
                
    except:
        pass        