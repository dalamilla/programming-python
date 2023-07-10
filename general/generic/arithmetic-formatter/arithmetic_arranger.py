def arithmetic_arranger(problems, flag=False):
  op1Array = []
  op2Array = []
  lineArray = []
  result = []
  separator = "    "

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    op = problem.split()
    lenght = max(len(op[0]), len(op[2])) + 2

    if op[1] != '+' and op[1] != '-':
      return "Error: Operator must be '+' or '-'."

    if len(op[0]) > 4 or len(op[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    if not op[0].isdigit() or  not op[2].isdigit():
      return "Error: Numbers must only contain digits."

    space1 = " " * (lenght - len(op[0]))
    op1Array.append(space1 + op[0])
    space2 = " " * (lenght - len(op[2]) - 1)
    op2Array.append(op[1] + space2 + op[2])

    lineArray.append("-" * lenght)

    if op[1] == '+': 
      spacer = " " * 2
      result.append(spacer + str(int(op[0]) + int(op[2])))
    
    if op[1] == '-': 
      spacer = " "
      result.append(spacer + str(int(op[0]) - int(op[2]))) 

  if flag:
    arranged_problems = f'{separator.join(op1Array)}\n{separator.join(op2Array)}\n{separator.join(lineArray)}\n{separator.join(result)}'
  else:
    arranged_problems = f'{separator.join(op1Array)}\n{separator.join(op2Array)}\n{separator.join(lineArray)}'

  return arranged_problems