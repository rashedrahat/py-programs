# a program that calculates everyday's productivity of skills.

import datetime

skill1_time = int(
    input("How many minutes you have given on front end? (HTML/CSS) : "))
skill2_time = int(
    input("How many minutes you have given on front end? (JS) : "))
skill3_time = int(
    input("How many minutes you have given on back end? (Python) : "))
history = {}


def skillHistory(total_time):
    today = datetime.date.today()
    history[today] = total_time
    print("Skills Audit History")
    print("--------------------")
    print(history, "%")


def measureProductivity(t1, t2, t3):
    total_skill_time = ((t1 + t2 + t3) / 480) * 100
    individual_skill1_time = (t1 / 120) * 100
    individual_skill2_time = (t2 / 180) * 100
    individual_skill3_time = (t3 / 180) * 100
    print("Your today's skill(s) audit:")
    print("----------------------------")
    print("Overall:", total_skill_time, "%")
    print("For HTML/CSS:", individual_skill1_time, "%")
    print("For JS:", individual_skill2_time, "%")
    print("For Python:", individual_skill3_time, "%")
    skillHistory(total_skill_time)


measureProductivity(skill1_time, skill2_time, skill3_time)
