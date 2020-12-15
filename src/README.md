# Running Truss

First, make sure python 3.8 (or aboved) is installed. Then, open a terminal and follow the steps:
1. Go to the directory where the codes are saved.
2. Set inputs in the **input.txt** file.
3. Run the command to execute Truss: <br/>
```python Control.py input.txt```
4. If the input sets are valid, an **output.txt** file will be generated.
5. To test input parameters, run <br/>
```python test_InParams.py```<br/>
(Note that you can add or modify test cases in the testcase_invalid file)
6. To test output correctness, run <br/>
```python test_OutCorrect.py```
7. You can see the code coverage reports in the **htmlcov** folder.
8. To analyze the coding standard, run <br/>
```flake8``` and <br/>
```pylint Control.py``` (or the other modules)
