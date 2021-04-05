def how_much_water(bricks_array: list) -> int:
    #return amount of water bricks
    #The iteration is saved too, to be able to scale the height down later on in the algorithm
    startgap = {"iteration": 0, "height": bricks_array[0]}
    tosub = 0
    bodies = 0
    amount = 0
    countup = True
    i = 1

    # I'm using a while loop to be able to jump back and forth in my list entries
    while i < len(bricks_array):
        # The loop starts if the next block is smaller than the highest previous spot
        if bricks_array[i] < startgap["height"]:
            # If it is not higher, the height of that block will later be subtracted
            tosub += bricks_array[i]
            # Used to calculate the amount of filled spots in gap
            bodies += 1
            # Checks if the loop arrived at the last entry
            if i == (len(bricks_array) - 1) and startgap["iteration"] != (len(bricks_array) - 1):
                # Do not count up the iteration
                countup = False
                # Lower the checking height to see if anything do fits and reset all stats
                startgap["height"] = startgap["height"] - 1
                bodies = 0
                tosub = 0
        # The new object is bigger or equal to the current object
        elif bricks_array[i] >= startgap["height"]:
            # Here the amount in the whole gap is calculated and recorded
            amount += (min(startgap["height"], bricks_array[i]) * bodies) - tosub
            # The new highest spot is marked and all data gets reset
            startgap["height"] = bricks_array[i]
            startgap["iteration"] = i
            bodies = 0
            tosub = 0

        # Simply an iteration counter, which manages also going back to a previous entry if line 22 comes into play
        if countup == True:
            i += 1
        else:
            i = startgap["iteration"] + 1
            countup = True

    return amount

listthing = [0, 3, 2, 4, 0, 2, 0, 4, 2, 0] # PUT YOUR ARRAY HERE
print(how_much_water(bricks_array=listthing))