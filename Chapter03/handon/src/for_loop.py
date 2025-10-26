subjects = [
    "Java",
    "C++",
    "JS",
    "Basic",
    "TypeScript",
    "Dart",
    "Kotlin"
]

def find_with_length(input: tuple[str, ...], size: int) -> tuple[str, ...]:
    result:list[str] = []

    for element in input:
        if len(element) == size:
            result.append(element)

    return tuple(result)



if __name__ == "__main__":
    result = find_with_length(tuple(subjects), 4)
    print(result)

    subject_dict:dict[int, str] = {}

    for id, subject in enumerate(subjects, start=1):
        subject_dict[id] = subject


    for entry in subject_dict.values():
        print(f"Entry is {entry}")
    