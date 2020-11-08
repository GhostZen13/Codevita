from itertools import combinations

def Philaland():
    
    testcase = int(input("Enter the number of testcases : "))
    item_cost = []
    final_combination = []
    count = 0
    for test in range(testcase):
        
        maximum_price = int(input("Enter the maximum price : "))
        k=1
        for k in range(1,(maximum_price+1)):
            item_cost.append(k)
            
        for element in combinations(item_cost,3): 
            if element[0] + element[1] == maximum_price: 
                final_combination.append((element[0],element[1]))
                
            else:
                continue
            
    
        print(final_combination)
        item_cost = []
            
            
            
            
Philaland()