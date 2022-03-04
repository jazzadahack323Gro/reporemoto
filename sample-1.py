with open(sys.argv[1]) as csv_file:
    reader = csv.reader(csv_file)

    data = list(reader)[1:]

data_by_column = list(zip(*data))

# This gives me the Control_ID column only.
control_ID = data_by_column[0]

# This gives me the Cost Column in ascending order. 
cost = (data_by_column[2])
cost = [ int(n) for n in cost]
cost1 = [ int(n) for n in cost]
cost_sorted = cost.sort(reverse = False)
print(cost1)

# This gives me the Value Column. 
value = (data_by_column[3])
value = [ int(n) for n in value ]
value1 = [ int(n) for n in value ]
value_sorted = value.sort(reverse = True)
print(value1)

# This gives us the value density
value_density = [i / j for i, j in zip(cost, value)]
print(str(value_density))

# This sets the count to zero.+
Counter = 0

# This counts the Control_ID column.
for i in control_ID:
    if i:
        Counter += 1

# This lists all possible control combinations. 
Possible_Control_Combinations = 2 ** Counter

# This is the start of my function.
def GetControlOptions(file_input, max_cost):
    
    print()
    
    # R6. Total Controls
    print('Total Controls: ', Counter)
    
    # R7. Possible Control Combinations
    print('Possible Control Combinations: ', Possible_Control_Combinations)
    
    print()
    
    # R8. Maximize Count Items
    print('Maximize Count Items: ',)
    
    # R9. Maximize Count Value
    print('Maximize Count Value: ',)
    
    print()
   


if __name__ == '__main__':
    file_input = ()
    max_cost = float(sys.argv[2])

GetControlOptions = GetControlOptions(file_input, max_cost)

exit()