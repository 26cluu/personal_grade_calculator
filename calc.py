from pymongo import MongoClient

cluster = MongoClient("mongodb://atricid:march292008@ac-iqugp7f-shard-00-00.hotiycd.mongodb.net:27017,ac-iqugp7f-shard-00-01.hotiycd.mongodb.net:27017,ac-iqugp7f-shard-00-02.hotiycd.mongodb.net:27017/?ssl=true&replicaSet=atlas-133991-shard-0&authSource=admin&retryWrites=true&w=majority")

db = cluster['grade_calc']
collection = db['grades']

def math_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'Math', 'assignment_type': 's'})]
    sum_total = [x['total'] for x in collection.find({'subject': 'Math', 'assignment_type': 's'})]
    form_correct = [x['correct'] for x in collection.find({'subject': 'Math', 'assignment_type': 'f'})]
    form_total = [x['total'] for x in collection.find({'subject': 'Math', 'assignment_type': 'f'})]

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    sum_percentage = sum(sum_correct) / sum(sum_total)
    form_percentage = sum(form_correct) / sum(form_total)
    return 0.75 * sum_percentage + 0.25 * form_percentage

def span_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'Spanish', 'assignment_type': 's'})]
    sum_total = [x['total'] for x in collection.find({'subject': 'Math', 'assignment_type': 's'})]
    form_correct = [x['correct'] for x in collection.find({'subject': 'Spanish', 'assignment_type': 'f'})]
    form_total = [x['total'] for x in collection.find({'subject': 'Spanish', 'assignment_type': 'f'})]

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    sum_percentage = sum(sum_correct) / sum(sum_total)
    form_percentage = sum(form_correct) / sum(form_total)
    return 0.8 * sum_percentage + 0.2 * form_percentage

def physics_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'Physics', 'assignment_type': 's'})]
    sum_total = [x['total'] for x in collection.find({'subject': 'Physics', 'assignment_type': 's'})]
    form_correct = [x['correct'] for x in collection.find({'subject': 'Physics', 'assignment_type': 'f'})]
    form_total = [x['total'] for x in collection.find({'subject': 'Physics', 'assignment_type': 'f'})]

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    sum_percentage = sum(sum_correct) / sum(sum_total)
    form_percentage = sum(form_correct) / sum(form_total)
    return 0.9 * sum_percentage + 0.1 * form_percentage

def history_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'History', 'assignment_type': 's'})]
    sum_total = [x['total'] for x in collection.find({'subject': 'History', 'assignment_type': 's'})]
    form_correct = [x['correct'] for x in collection.find({'subject': 'History', 'assignment_type': 'f'})]
    form_total = [x['correct'] for x in collection.find({'subject': 'History', 'assignment_type': 'f'})]

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    sum_percentage = sum(sum_correct) / sum(sum_total)
    form_percentage = sum(form_correct) / sum(form_total)
    return 0.7 * sum_percentage + 0.3 * form_percentage

def scripture_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'Scripture', 'assignment_type': 's'})]
    sum_total = [x['total'] for x in collection.find({'subject': 'Scripture', 'assignment_type': 's'})]
    form_correct = [x['correct'] for x in collection.find({'subject': 'Scripture', 'assignment_type': 'f'})]
    form_total = [x['total'] for x in collection.find({'subject': 'Scripture', 'assignment_type': 'f'})]

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    # sum_percentage = sum(sum_correct) / sum(sum_total)
    # form_percentage = sum(form_correct) / sum(form_total)
    # return 0.7 * sum_percentage + 0.3 * form_percentage

    return (sum(sum_correct) + sum(form_correct)) / (sum(sum_total) + sum(form_total))

def english_calc(type, correct, total):
    sum_correct = [x['correct'] for x in collection.find({'subject': 'English', 'assignment_type': 's'})] 
    sum_total = [x['total'] for x in collection.find({'subject': 'English', 'assignment_type': 's'})] 
    form_correct = [x['correct'] for x in collection.find({'subject': 'English', 'assignment_type': 'f'})] 
    form_total = [x['total'] for x in collection.find({'subject': 'English', 'assignment_type': 'f'})] 

    if type == 'f':
        form_correct.append(correct)
        form_total.append(total)
    if type == 's':
        sum_correct.append(correct)
        sum_total.append(total)

    sum_percentage = sum(sum_correct) / sum(sum_total)
    form_percentage = sum(form_correct) / sum(form_total)
    return 0.7 * sum_percentage + 0.3 * form_percentage



# subject = input('Please type which subject you want to calculate: ')
# type_grade = input('Please say whether the subject is f, s, or none: ')
# correct = int(input('Correct Points: '))
# total = int(input('Total: '))

# if subject == 'math':  
#     print(math_calc(type_grade, correct, total))
# if subject == 'spanish':
#     print(span_calc(type_grade, correct, total))
# if subject == 'physics':
#     print(physics_calc(type_grade, correct, total))
# if subject == 'history':
#     print(history_calc(type_grade, correct, total))
# if subject == 'scripture':
#     print(scripture_calc(type_grade, correct, total))
# if subject == 'english':
#     print(english_calc(type_grade, correct, total))

