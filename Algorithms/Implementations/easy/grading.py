# Problem URL https://www.hackerrank.com/challenges/grading

def roundGrade(grade):
    if(grade < 38):
        return grade
    else:
        fract = grade%5
        if(fract>=3):
            grade = grade - fract + 5
        return grade

def main():
    for x in xrange(int(raw_input().strip())):
        print(roundGrade(int(raw_input().strip())))
    
if __name__ == '__main__':
    main()