# Chapter 1 Assignment - Hello Python

After completing this lesson, you should understand:
- How to setup python project in VS Code
- How to organize source file inside a src/ folder
- How to write and run unit test using pytest

## Assignment Instruction

1. Create a new folder named my-first-project (this will be the project base).
2. Inside the assignment folder, create two subfolders:
    - src → for your Python scripts
    - tests → for your test cases
3. In the src folder, create a file named calculator.py.
4. Inside calculator.py, write a function named add_integer that:
    - Takes two integers as arguments
    - Returns their sum
    - Example: add_integer(2, 3) → 5
5. In the tests folder, create a file named test_calculator.py.
6. In test_calculator.py, write a test function named test_add_integer that checks if your add_integer function works correctly.
    - Hint: Use assert to compare the expected result with the actual result.
    ```
    def test_add_integer():
        assert add_integer(2, 3) == 5
        assert add_integer(-1, 1) == 0
    ```
7. Run your test case using pytest and make sure all tests pass successfully.

✅ Goal: By the end, you’ll have a working project structure with a function and a passing test case.
