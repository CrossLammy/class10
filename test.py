# function
def cal_grade(quiz,midterm,final):
    sum_score=quiz*0.2+midterm*0.4+final*0.4
    if sum_score >=80:
        grade='A'
    elif sum_score >=70:
        grade='B'
    elif sum_score >=60:
        grade='C'
    elif sum_score >=50:
        grade='D'
    else:
        grade='F'
    return grade,sum_score

qPoint=float (input("ระบุ'คะแนนเก็บ'ทั้งหมด[100]:"))
mPoint=float (input("ระบุ'คะแนนMidTerm'[100]:"))
fPoint=float (input("ระบุ'คะแนนFinal'[100]:"))

theGrade,theScore=cal_grade(qPoint,mPoint,fPoint)

print(f"คุณได้เกรด:{theGrade} คะแนน {theScore}")
