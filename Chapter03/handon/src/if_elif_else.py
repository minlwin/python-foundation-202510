def check_grade(mark: int) -> str:
    result = "Fail"

    if mark >= 0 and mark < 40 :
        result = "Fail"
    elif mark >= 40 and mark < 80:
        result = "Pass"
    elif mark >= 80 and mark <= 100:
        result = "Excellent"
    else :
        result = "Impossible"
    
    return result