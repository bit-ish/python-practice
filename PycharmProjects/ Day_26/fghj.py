students=["a","b","c","d","e","t"]
import random
students_marks={student:random.randint(1,100) for student in students}
passed_students={student:mark for (student,mark) in students_marks.items() if mark>50}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence1=sentence.split()
result = {word:len(word) for word in sentence1}
print(result
      )
