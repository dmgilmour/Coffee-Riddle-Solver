# Coffee-Riddle-Solver

Decided to solve the 538 Coffee Addiction riddler by running some simulations. The problem can be found here: https://fivethirtyeight.com/features/can-you-drink-more-coffee-than-your-coworkers/

The rules are that there is 1 coffee pot in the office and you want to get as much coffee as possible and don't want to refill the pot. Select a fraction of the total coffee pot's volume that you will attempt to pour in your mug. If you take the last bit of coffee you must refill the coffee pot, and are so angry about this that you break your mug and get no coffee at all. 

Figure out how much coffee you should take per trip to maximize the coffee you get over the course of several lifetimes in this office (thousands of simulations).

## Results

I first ran the simulation with an even spread of coffee grab attempts, so each of 100 employees would take a different percent from 0 to 99% of the pot. This gave an optimal result very near the top, around 0.99. I then simulated what the optimal proportion to take would be for differing mean population responses. To do this I left the above employees to test what proportion returns the maximum percent while adding a large number of new dummy employees who would all take the same proportion, meaning a significant majority of the total employees would be taking the same proportion. I tested this for approximately each .01 proportion running 5000 simulations of 300 employees and got the following scatter plot:

![alt text](http://i.imgur.com/2apeGr7.png "")

The lower values on the X-axis have more samples because I wanted more precise data to show a trend.

From right to left, the slopes of the lines are 0, -1, -2, ... etc. Each distinct line represents the average number of trips to take coffee before it's all taken. So with the line on the furthest right, only one employee will get coffee before the pot is emptied, so the logical thing to do is take as much as possible. 

Observing the edge of the right and second to the right lines, an average of two employees can get coffee before the pot's empty, so there are three options, you'll either get there when it's full, get there when roughly half is taken, or get there when it's nearly all taken. If you opt to take half, you have a 2 in 3 chance of gettin 0.5, if you try to take all, you have a 1 in three chance of getting 1.0, which is equivalent. If the average employee is taking less than half, but more than could fit in three trips, the best strategy is to maximize the amount of coffee you could get if one person came before you, so take 1 - avg, which is why this line has a slope of -1.

The next line we would expect to occur would be when we could fit 3 trips in (0.25 - 0.33) Which gives us four possible approaches: 25% chance of 1, 50% chance of 0.66, or 75% chance of 0.33. However in this case the 50% chance of 0.66 is still the best option, so you should still try to take 0.66.

Next would be 4 trips (0.2 - 0.25) with options: 20% of 1, 40% of 0.75, 60% of 0.5, or 80% of 0.25. In this case we get equal returns on  40% of 0.75 and 60% of 0.5, which gives us the next edge.

Next would be 5 trips (0.1667 = 0.2) with options: 16.7% of 1, 33% of 0.8, 50% of 0.6, 66.7% of 0.4, or 83.3% of 0.2. Which gives us an optimal solution of 50% of 0.6


In coming up with my submission, I noticed that it is never a good idea to take less than 50% of the pot. Because we're assuming the population is rational, we only have to look above the 0.5 average population response marker for the optimal amount to take, and no matter the average response, the correct solution is to take as much as possible. 
