using System;

namespace DaveO.AdventOfCode.Day3
{
    class Program
    {
        static void Main(string[] args)
        {
            var records = Rate.GetRates();
            int countOnes = 0;
            int countZeros = 0;

            for (int i = 0; i <= 11; i++)
            {
                countOnes = 0;
                countZeros = 0;
                foreach (var rate in records)
                {
                    if (Rate.IsOne(rate.values[i]))
                    {
                        countOnes = countOnes + 1;
                    }
                    else
                    {
                        countZeros = countZeros + 1;
                    }
                }
                Console.WriteLine("{2} bit: Ones:{0}, zeros:{1} ", countOnes, countZeros, i+1);
            }
            Console.ReadLine();
        }
    }
}
