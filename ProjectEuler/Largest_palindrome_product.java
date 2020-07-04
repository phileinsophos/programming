/*
	Problem Statement : Largest palindrome product
	Link : https://projecteuler.net/problem=4
	Score : accepted
*/
import java.io.*;
import java.lang.*;

class Largest_palindrome_product
{
	public static void main(String args[])
	{
		int a=900,b=999;
		long x=0L,lar=0L;
		String a1="",b1="";
		for(int i=a;i<=b;i++)
		{
			for(int j=a;j<=b;j++)
			{
				x=i*j;
				a1=""+x;
				b1 = new StringBuffer(a1).reverse().toString();
				if(b1.equalsIgnoreCase(a1))
				{
					lar=x;
					System.out.println(i+"*"+j+"=="+lar);
				}	
			}
		}
		System.out.println("\n\n"+lar);
	}
}
