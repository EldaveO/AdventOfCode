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

            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value1))
                {
                    countOnes = countOnes++;
                }
                else
                {
                    countZeros = countZeros++;
                }
            }
            Console.WriteLine(countZeros);
            Console.ReadLine();
        }
    }
}
