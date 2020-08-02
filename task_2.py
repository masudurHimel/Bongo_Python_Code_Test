
def print_depth(data):
    """ 
    Prints all the keys with their corresponding depth
    [Can handle python object as well in dictionary]

    Parameters: 
    data (dict): passed dictionary to work 

    Returns: 
    str: Containing all the keys with their corresponding depth in sorted order where index is the depth
    """

    if type(data) not in [dict]:
        raise TypeError("Passed Arguement must be a dictionary !")

    result = []
    process_dict(data)

    count = 1
    
    for i in data.keys():
        result.append((i,count))

    levels = [(i, count + 1) for i in data.values() if isinstance(i, dict)]

    while(levels):
        key, count = levels.pop()
     
        for i in key.keys():
            v = key[i]
            if isinstance(v, dict):
                result.append((i,count))
                count += 1
                levels.append((v,count))
            else:
                result.append((i,count))
                
    sorted_result = result
    sorted_result = sorted(sorted_result, key = lambda x: x[1])     
    
    result_str = ""
    
    for i in range(len(sorted_result)):
        result_str= result_str + str(sorted_result[i][0])+ " " + str(sorted_result[i][1]) + "\n"
    
    result_str = result_str[:-1]
    return result_str   

def process_dict(data):
    """ 
    Convert the objects into dictionary 

    Parameters: 
    Data (dict): passed dictionary to modify 

    Returns: 
    None; Just modifies the original dictionary
    """

    if type(data) not in [dict]:
        raise TypeError("Passed Arguement must be a dictionary !")
    
    instanceFinder = []
    
    for i in data.keys():
        v = data[i]
        if isinstance(v,dict):
            instanceFinder.append(v)
        elif isinstance(v, Person):
            data[i] = {'first_name': v.first_name, 'last_name': v.last_name, 'father': v.father}
            v = data[i]
            instanceFinder.append((v))
       
    while(instanceFinder):
        key= instanceFinder.pop()
        
        for i in key.keys():
            v = key[i]
            if isinstance(v, Person):
                
                key[i] = {'first_name': v.first_name, 'last_name': v.last_name, 'father': v.father}
                v = key[i]
                instanceFinder.append((v))
                
            if isinstance(v, dict):
                instanceFinder.append((v))
                



class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

if __name__=="__main__":
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)

    target_dict = { "key1": 1, "key2": { "key3": 1, "key4": { "key5": 4, "user": person_b}}}
    print(print_depth(target_dict))
