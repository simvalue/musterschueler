import math
#Hier die (erwarteten) Punkte einfüllen
test_1 = 50 #Erster Test
test_2 = 20 #Zweiter Test
shorttest_total = 3 #Alle punkte von kurztests
num_ue = 11 #10 falls man bei ersten tutorium noch nicht dabei war
total_ue_tasks = 3*num_ue 
tasks_done = 17 #Anzahl der erledigten Aufgaben (1 UE = 3 Aufgaben, erledigt bedeutet min 1 punkt) 
ue_points_total = 90
worst_ue_points = 0#Punkte auf schlechteste Übung (wird gestrichen) ACHTUNG: Außer ihr wurdet an der Tafel schlechter bewertet!
is_berufstaetig = False

#Ab hier implementierung der punkteformel, sollte nicht verändert werden müssen
shorttest_normed = (shorttest_total / 20)*20 #ACHTUNG: Normierung kurzztest punkte nicht bekannt bisher, könnten weniger zählen!
shorttest_grade = min(shorttest_normed, 10)
shorttest_bonus = shorttest_normed-shorttest_grade


max_ue_points = 9*(num_ue-1) #gestrichene UE mitbeachten
ue_points_total = ue_points_total - worst_ue_points
ue_points_normed = ue_points_total*(40/max_ue_points)
ue_points_grade = min(ue_points_normed, 20)
ue_points_bonus = ue_points_normed - ue_points_grade

tasks_done_ratio = round(tasks_done/total_ue_tasks, 1)

if is_berufstaetig:
    total_points = math.floor(200*(test_1+test_2+ue_points_grade)/220 + ue_points_bonus)
    print(f"Punkteformel: P = 200*(T_1+T_2+U_1)/230 + U_2 = 200*({test_1}+{test_2}+{ue_points_grade})/220 + {ue_points_bonus} = {total_points}")
total_points = math.floor(200*(test_1+test_2+shorttest_grade+ue_points_grade)/230 + shorttest_bonus + ue_points_bonus)
print(f"Punkteformel: P = 200*(T_1+T_2+K_1+U_1)/230 +K_2 + U_2 = 200*({test_1}+{test_2}+{shorttest_grade}+{ue_points_grade})/230 + {shorttest_bonus} + {ue_points_bonus} = {total_points}")

passed = True
if total_points >= 81 :
    print(f"Gesamtpunkte {total_points} reichen aus!")
else:
    print(f"Es fehlen insgesamt noch {math.ceil(81 - total_points)} punkte zum bestehen!")
    passed = False

if test_1 < 20 or test_2 < 20:
    print(f"Beide Tests müssen mindestens 20 Punkte haben")
    passed = False

if tasks_done_ratio < 0.5:
    tasks_needed = math.ceil(total_ue_tasks*0.5)
    tasks_left = tasks_needed - tasks_done
    print(f"Es müssen mindestens {tasks_needed} aufgaben erledigt werden, es fehlen noch {tasks_left}")
    passed = False

if not passed:
    print("Aktuell würdest du die VU leider nicht bestehen!")
else:
    grade = 4
    if total_points > 110:
        grade = grade - 1
    if total_points > 140:
        grade = grade - 1
    if total_points > 170:
        grade = grade - 1
    if total_points > 190:
        print(f"Absolutes Strebertum erreicht!")
    
    print(f"Glückwunsch! Du wirst die UE mit Note {grade} bestehen! Alle Angaben ohne Gewähr")





