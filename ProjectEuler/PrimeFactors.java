/*
  Problem Statement : Largest prime factor
  Link : https://projecteuler.net/problem=3
  Score : accepted
*/	
import java.io.*;
class PrimeFactors
{
public static void main(String args[]) throws IOException
{
BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
Long n=600851475143L;
long i=2L,x=0L;
while(n>1)
  {
   if(n%i == 0)
    {
     x=i;
     n=n/i;
    }
   else
    i++;
  }
System.out.print(x+"\n");  
}
}
