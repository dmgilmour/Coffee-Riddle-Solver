# Coffee-Riddle-Solver

Decided to solve the FiveThirtyEight Coffee Addiction riddler by running some simulations. The problem can be found here: https://fivethirtyeight.com/features/can-you-drink-more-coffee-than-your-coworkers/

The rules are that there is 1 coffee pot in the office and you want to get as much coffee as possible and don't want to refill the pot. Select a fraction of the total coffee pot's volume that you will attempt to pour in your mug. If you take the last bit of coffee you must refill the coffee pot, and are so angry about this that you break your mug and get no coffee at all. 

Figure out how much coffee you should take per trip to maximize the coffee you get over the course of several lifetimes in this office (thousands of simulations).

## Results

I first ran the simulation with an even spread of desired volumes. Each of 100 employees would take a different percent from 0 to 99% of the pot. This gave an optimal result very near the top, around 0.99. I then simulated what the optimal proportion to take would be for differing mean population responses. To do this I left the above employees to cover a wide range of possible optimal responses, while adding a large number of new employees who would all take the same proportion, meaning a significant majority of the total employees would be taking the same proportion. The simulations gave the following scatterplot:

![alt text](http://i.imgur.com/jQk13RB.png "")

(The lower values on the x axis have more samples because I wanted more precise data to show a trend)

The rightmost line from (0.5 - 1.0 on the x axis) represents only being able to fit one employee's coffee trip before a second of the same value would take the last of the coffee. On this line, you have a 50% chance of getting whatever you requested, and therefore the best solution is to take nearly the entire pot, limit approaching 1.0

Observing the edge of the right and second to the right lines (0.5 on x), an average of two employees can get coffee before the pot's empty, so there are three options: you'll either get there when it's full, get there when roughly half is taken, or get there when it's nearly all taken. If you opt to take half, you have a 66% chance of gettin 0.5, if you try to take all, you have a 33% chance of getting 1.0, which are equivalent. If the average employee is taking less than half, but more than could fit in three trips, the best strategy is to maximize the amount of coffee you could get if one person came before you, so take  `1 - AVG`.

The next line we would expect to occur would be when we could fit 3 trips in (0.25 - 0.33) which gives us four possible approaches: 25% chance of 1.0, 50% chance of 0.66, or 75% chance of 0.33. However in this case the 50% chance of 0.66 is still the best option, so you should still try to take 0.66.

Next would be 4 trips (0.2 - 0.25) with options: 20% of 1.0, 40% of 0.75, 60% of 0.5, or 80% of 0.25. In this case we get equal returns on  40% of 0.75 and 60% of 0.5, which gives us the next edge. In this section you're maximizing how much you can get after two trips from the population mean, which means you should try to get the remaining amount of  `1 - 2*AVG`

## Trends on Trends on Trends

The trend looking from right to left is a new line appears when you maximize how much you get by attempting to take the remaining pot when you assume there was a certain number of trips before you arrived. This line has a slope of  `-(Trips Expected Before You)`

Here is the true trend simulated in the program:

![alt text](http://i.imgur.com/A4A050Q.png "")

In coming up with my submission, I noticed that it is never a good idea to take less than 50% of the pot. Because we're assuming the population is rational, we only have to look above the 0.5 average population response marker for the optimal amount to take, and no matter the average response, the correct solution is to take as much as possible. 
