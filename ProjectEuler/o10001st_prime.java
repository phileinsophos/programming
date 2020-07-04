/*

	Problem Statement : 10001st prime
	Link : https://projecteuler.net/problem=7
	Score : acceped
	
*/

import java.io.*;
import java.util.*;
class o10001st_prime
{	
	public static void main(String args[])
	{
		long x=0L,n=0L;
		
		for(int i=2;i>0;i++)
		{
		int f=1;
			for(int j=2;j<i;j++)
			{
				if(i%j==0)
					f=0;
			}
			if(f==1)
			{
				n++;
				x=i;
			//	System.out.println(x+" = "+n);
			}	
			if(n==10001)
			{
				System.out.println("\n\n"+x);
				break;
			}	
		}
	}
}
