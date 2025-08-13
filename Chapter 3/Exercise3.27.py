currentPopulation = 8233493530L;
growthRate = 0.9512;
numberOfYears = 75;
totalPopulation = 0;

for(int yearCount = 1; yearCount <= numberOfYears; yearCount++){
	for (int output = 1; output <= 1; output++) {
		double population = currentPopulation * Math.pow((1 + growthRate),1);
		totalPopulation += population;
		System.out.print("Year " + yearCount + ": " + totalPopulation);
	}
System.out.println();
