def print_depth(data):
    """ 
    Prints all the keys with their corresponding depth 

    Parameters: 
    data (dict): passed dictionary to work

    Returns: 
    str: Containing all the keys with their corresponding depth in sorted order where index is the depth
    """
    if type(data) not in [dict]:
        raise TypeError("Passed Arguement must be a dictionary !")

    result = {}
    count = 1

    for i in data.keys():
        result[i] = count

    levels = [(i, count + 1) for i in data.values() if isinstance(i, dict)]

    while(levels):
        key, count = levels.pop()
     
        for i in key.keys():
            v = key[i]
            if isinstance(v, dict):
                result[i] = count
                count += 1
                levels.append((v,count))
            else:
                result[i] = count           

    final_result = sorted(result.items(), key = lambda x:x[1])

    result_str = ""
    
    for i in range(len(final_result)):
        result_str= result_str + str(final_result[i][0])+ " " + str(final_result[i][1]) + "\n"
    
    result_str = result_str[:-1]
    return result_str

if __name__=="__main__":
    target_dict = {"key1": 1,"key2": {"key3": 1,"key4": {"key5": 4}}}
    print(print_depth(target_dict))