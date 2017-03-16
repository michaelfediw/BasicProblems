def simple_robot_localization(surroundings, location):
    '''
    (list, int) -> (str)
    
    One-dimensional robot localization program.
    Input: a list that defines the realm where the robot resides. It consists of 
    either 'white' or 'black' locations.
    eg: ['white', 'white', 'white', 'black', 'black', 'white', 'black']
    
    Input: an integer defining the robot's starting position in the list. 
    eg: 1 would say that the robot is starting at index 1 of the list that defines 
    the robots location.
    
    Output: the robots starting location (ie the location value that is passed to the 
    function)
    
    RULES: 
    1). The robot can only move one 'location' to the right at a time.
    2). The robot can sense the color of it's current location.
    
    '''
    
    start = location
    surroundings.append('end')
    length = list(range(len(surroundings)))
    
    current_location = start  
    
    color = surroundings[current_location]
    
    
    poss_start = []
    
    
    for i in length:
        if surroundings[i] == color:
            poss_start.append(i)
    
    count = 1
    
    while len(poss_start) > 1:
        current_location += 1
        poss_start_copy = []
        color = surroundings[current_location]
    
        for i in poss_start:
            if surroundings[i+count] == color:
                poss_start_copy.append(i)
        
        poss_start = poss_start_copy
        count += 1
    
    
        
    return poss_start