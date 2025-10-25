def get_status(status:int) -> str:
    result = ""
    
    match status:
        case 200:
            result = "Success"
        case 300:
            result = "Redirect"
        case 400:
            result = "Bad Request"
        case 500:
            result = "Internal Server Error"
        case _:
            result = "Other Status"

    return result

def get_grade(value : int) :
    result = ""

    match value:
        case m if m >= 0 and m < 40:
            result = "Fails"
        case m if m >= 40 and m < 80:
            result = "Pass"
        case m if m >= 80 and m <= 100:
            result = "Excellent"
        case _:
            result = "Impossible" 
    return result

if __name__ == "__main__":
    print(get_status(100))
    print(get_grade(500))