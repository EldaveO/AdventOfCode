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
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("1 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value2))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("2 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value3))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("3 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value4))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("4 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value5))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("5 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value6))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("6 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value7))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("7 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value8))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("8 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value9))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("9 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value10))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("10 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value11))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("11 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            countOnes = 0;
            countZeros = 0;
            foreach (var rate in records)
            {
                if (Rate.IsOne(rate.value12))
                {
                    countOnes = countOnes + 1;
                }
                else
                {
                    countZeros = countZeros + 1;
                }
            }
            Console.WriteLine("12 bit: Ones:{0}, zeros:{1} ", countOnes, countZeros);

            Console.ReadLine();
        }
    }
}
