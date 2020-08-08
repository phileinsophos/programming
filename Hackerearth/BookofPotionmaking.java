/*
		Problem Statement : Book of Potion making
		Link :https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/
		Score : 20

*/

import java.util.*;

class BookofPotionmaking
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		String isbn=sc.nextLine();
		int sum=0;
		if(isbn.length()!=10)
			System.out.println("Illegal ISBN");
		else
		{
			for(int i=0;i<10;i++)
			{
				int n=Character.getNumericValue(isbn.charAt(i));
				sum=((i+1)*n)+sum;
			}
			if(sum%11==0)
				System.out.println("Legal ISBN");
		}

	}
}
