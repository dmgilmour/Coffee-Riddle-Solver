import java.util.Random;
import java.util.Scanner;
import java.io.*;

public class CoffeeSolver {
	
	public static void main(String[] args) {

		Random rand = new Random(System.currentTimeMillis());

		int simulations = Integer.parseInt(args[0]);
		int numEmployees = Integer.parseInt(args[1]);
		float mean = Float.parseFloat(args[2]);

		double[][] coffeeDrinkers = new double[numEmployees][3];

		for (int i = 0; i < numEmployees; i++) {
			do {
				coffeeDrinkers[i][0] = rand.nextGaussian() * .2 + mean;
			} while (coffeeDrinkers[i][0] > 1 || coffeeDrinkers[i][0] < 0);
		}

		for (int i = 0; i < simulations; i++) {
			runSimulation(coffeeDrinkers);
			randomizeOrder(coffeeDrinkers, rand);
		}

		File outFile = null;
		outFile = new File("output.txt");
		PrintWriter print = null;
		try {
			print = new PrintWriter(outFile);
		} catch (Exception e) {}

		double max = 0;
		double maxLoc = 0;
		for (double[] employee : coffeeDrinkers) {
			if (employee[1] > max) {
				max = employee[1];
				maxLoc = employee[0];
			}
	
			print.println(employee[0] + ", " + employee[1] + ", " + employee[2]);
		}
		System.out.println("Winner is " + maxLoc);

		print.close();
	}

	public static void runSimulation(double[][] coffeeDrinkers) {
		
		double coffeePot = 1.0;

		for (double[] employee : coffeeDrinkers) {
			coffeePot -= employee[0];
			if (coffeePot < 0) {
				coffeePot = 1.0;
				employee[2] += 1;
			} else {
				if (employee[0] > 1) System.out.println("wtf");
				employee[1] += employee[0];
			}
		}
	}

	public static void randomizeOrder(double[][] coffeeDrinkers, Random rand) {
		
		double[] temp;
		int randLoc;
		int arrSize = coffeeDrinkers.length;
		for (int i = 0; i < arrSize; i++) {
			randLoc = rand.nextInt(arrSize);
			temp = coffeeDrinkers[randLoc];
			coffeeDrinkers[randLoc] = coffeeDrinkers[i];
			coffeeDrinkers[i] = temp;
		}
	}
}	
