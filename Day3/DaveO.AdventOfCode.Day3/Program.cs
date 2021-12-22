using System;

namespace DaveO.AdventOfCode.Day3
{
    class Program
    {
        static void Main(string[] args)
        {
            var o2Records = Rate.GetRates();
            var co2Records = Rate.GetRates();

            for (int i = 0; i < 12; i++)
            {
                int countOnes = 0;
                int countZeros = 0;
                Console.WriteLine();
                Console.WriteLine(" Checking position {0}", i+1);
                Console.ReadLine();

                foreach (var rate in o2Records)
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

                //Console.WriteLine("ONES:{0}, ZEROS:{1}", countOnes, countZeros);
                o2Records = BitCriteria.KickOut(o2Records, countOnes, countZeros, "o2", i);
                
                foreach (var rate in o2Records)
                {
                    //Console.WriteLine(" {0} o2 records left", o2Records.Count);
                    for (int c = 0; c < 12; c++)
                    {
                        Console.Write(rate.values[c]);
                    }
                    Console.WriteLine();
                }
            }
            Console.WriteLine();
            Console.WriteLine(" Final o2 record:! {0} ! ", o2Records.Count);
            Console.WriteLine();
            Console.ReadLine();
        }
    }
}
