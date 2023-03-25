n = int(input()) # n refers to the number of student, it should be an integer
for i in range(n): # i refers to the ordinal number of an exact student
    student_info = input().split() # This loop is wrongly idented
    weighted_score = 0
    pla_times = 0
    for j in range(1, 4): # Here should define another variable to refer to the ordinal of assignment. Moreover, a range of nuber include the left side but not the right side
        if (student_info[j] == "plagiarism"): # "==" is used to estimate whether two value are equivalent
            student_info[j] = 0
            pla_times = pla_times + 1
        else:
            student_info[j] = int(student_info[j]) # Here we should transform the data type into integer
    if (pla_times == 2):
        weighted_score = 0
    else:
        weighted_score = (0.2 * student_info[1] + 0.3 * student_info[2] + 0.5 * student_info[3] )//1  
    print(student_info[0]+'\'s weighted score is',int(weighted_score))