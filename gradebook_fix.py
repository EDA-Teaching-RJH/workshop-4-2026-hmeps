def main():

    student_count = int(input("How many students to enter? "))

    names = []
    scores = []

#originally had print("student: "+ i + 1) so changed with a comma as you cant just + i
    for i in range(student_count):
        print("Student: ",i + 1)

#had to express .strip() AND .title() as individual functions, NOT the same as names.append where .append() is the only function
        name_input = (input("Name: ")).strip().title()
        names.append(name_input)

        while True:
            score_input = int(input("Score: "))
            
            # Check for valid range
            if score_input < 0 or score_input > 100:
                print("Invalid score. Must be 0-100.")
                continue
            else:
                break
        
        scores.append(score_input)

    print("--- Class Summary ---")
    
#the scores list uses [] but this bit originally had i in () instead so was an easy fix
    for i in range(len(names)):
        if scores[i] < 40:
            result = "Fail"
        else:
            result = "Pass"
        
        print(f"{i + 1}: {names[i]} - {scores[i]} ({result})")

#always remember to callback to main with () at the end when using functions
main()