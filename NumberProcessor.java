public class NumberProcessor {
	/**
	* This method returns
	*/
	public static int mirrorNum(int num){
		int ones = 0; // the ones column of the num, last num on right
		int sums = 0; //the final number flipped
		while (num != 0) { // while the input is not zero/there are no nums left
			ones = num % 10; //takes the num at the end
			num /= 10; // rids of last num
			sums = (sums * 10) + ones; // moves num to the right & adds last num
		}
		return sums; // returns reversed num
	}
		

	/**
	* This method returns
	*/
	public static int stripOdds(int input) {
		int ones = 0; // the last num at end of number in ones column
		int ans = 0; // the answer
		int count = 0; // counts how many zeroes at the end there are
		while (input % 10 == 0) { // while num has a 0 at end
			count ++; // increments
			input /= 10; // cuts off end
		}
		int mirrored = mirrorNumber(input); // mirrors number
		while (mirrored != 0) { // goes through the whole num, stops when none left
			ones = mirrored % 10; // looks at ones
			if (ones % 2 == 1) { // if odd
				mirrored /= 10; // slice end & continue
			}
			else if (ones % 2 == 0) { // if even
				ans = ans * 10 + ones; // add to answer
				mirrored /= 10; // cuts off end
			}
		}
		for (int i = 0; i < count; i ++) {
			ans *= 10; // adds the zeroes at the end that were there b4
		}
		return ans;
	}
		// public static void main(String[] args){
		// 	System.out.println(stripOdds(556550));
		// 	System.out.println(stripOdds(6770));
		// 	System.out.println(stripOdds(12304));
		// 	System.out.println(stripOdds(2300));
		// }

	/**
	*
	* This method returns
	*
	*
	*/
	
	public static boolean hasHiddenPrime(long input) {
		// DELETE THE LINE BELOW ONCE YOU IMPLEMENT THE CALL!
		// throw new RuntimeException("not implemented!");
		while (input != 0) {
			if (input <= 1) {return false;}
			else {
				for (int i = 2; i < input; i++) {
					if (input % i == 0) {return false;}
				}
			}
		}
		return false;
	}


	/**
	* This method returns true if
	*/
	public static boolean isCozyNumber(int input1, int input2) {
		if (input1 == input2) {return true;} // if nums are equal to each other -> cozy
		if (input2 > input1) {return false;} // if in2 is bigger, can't be found in in1
		while (input1 != 0) { //when there is no more of input1
			if (input1 % 10 != input2 % 10) { // if last num of both aren't equal
				input1 /= 10; // cuts off last num of in1..
				continue; // ..& repeats through loop
			}
			else if (input1 % 10 == input2 % 10) { // if last nums are same
				if ((input1 / 10) % 10 != ((input2 / 10) % 10)) { // & num after aren't
					input1 /= 10; // slices and continues through checking
					continue;
				}
				else {break;} // exits loop when match found & next num matches 2
			}
		}
		if (input1 % 10 == input2 % 10) { // if last num matches
			while (input2 % 10 == input1 % 10) { // while there's still input2
				input1 /= 10; // slices off end of input1
				input2 /= 10; // slices off end of input2
				if (input2 == 0 || input1 == 0) {break;} // if either nums reach end
			} 
			if (input2 == 0) {return true;} // 
		}
		return false;
	}
		// public static void main(String[] args){
		// 	System.out.println(isCozyNumber(9, 9));
		// 	System.out.println(isCozyNumber(9, 7));
		// 	System.out.println(isCozyNumber(270, 70));
		// 	System.out.println(isCozyNumber(107744, 74));
		// 	System.out.println(isCozyNumber(7, 17));
		// }	

	/**
	 *
	 * This method returns true if
	 *
	 */
	public static boolean isNumberJackWinner(int[] array){
		int[] arr = array;
		if (arr.length != 3) {return false;}
		int sums = 0;
		for (int i = 0; i < 3; i ++) {
			if (arr[i] > 0 && arr[i] < 11) {
				sums += arr[i];
			}
		}
		if (sums >= 17 && sums <= 21) {return true;}
		else {return false;}
	}

	
	// public static void main(String[] args){
	// 	int[] x = {1, 1, 1};
	// 	System.out.println(isNumberJackWinner(x));
	// }

	/**
	 *
	 * This method returns
	 *
	 */
	public static int[][] array2matrix(int[] array){
		int[][] arr = new int[array[0]][array[1]]; // creates new array w given dimensions
		int k = 2;
		for (int i = 0; i < array[0]; i ++) { // accesses rows of array
			for (int j = 0; j < array[1]; j ++) { //accesses columns
				while (k < array.length) {
					arr[i][j] = array[k]; // puts one value in
					k ++;
					break; // moves to next coord after putting in
				}
			}
		}
		return arr;
	}
	public static void main(String[] args){
		int[] x = {2, 1, 3};
		System.out.println(array2matrix(x));
	}

	/**
	 * This methods returns
	 */
	public static void shootBattleCraft(int[][] battleMap, int[][] shotCoordinates) {
		for (int i = 0; i < shotCoordinates.length; i ++) { // accessing coords
			int x = shotCoordinates[i][0];
			int y = shotCoordinates[i][1];
			if (battleMap[x][y] > 0) {
				battleMap[x][y] = -1;
			}
		}
	}
	

	/**
	 *
	 * Main method. Is not tested by the tester, create your own tests here!
	 */
	// public static void main(String[] args){
		//pass
	// }
	}

