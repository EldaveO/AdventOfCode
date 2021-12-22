using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DaveO.AdventOfCode.Day3
{
    class BitCriteria
    {
        //fields

        //constructors
        public BitCriteria() { }

        //properties

        //methods

        //find most common value 1 0 or equal
        //kick out the values that are the least common based on bit placement
        // if only one value left in collection then print
        public static List<Rate> KickOut(List<Rate> rates, int ones, int zeros, string type, int position)
        {
            List<Rate> tempRates = new List<Rate>(rates);

            int i = 0;

            if (ones > zeros) //kick out zeros
            {
                foreach (var rate in rates)
                {
                    if (rate.values[position] == 0)
                    {
                        Console.WriteLine(rate.values[position]);
                        tempRates.RemoveAt(i); 
                    }
                }
                i = i + 1;
                return tempRates;
            }
            else if (ones < zeros) //kick out ones
            {
                Console.WriteLine("removing all ones! index {0}", i);
                foreach (var rate in rates)
                {

                    if (rate.values[position] == 1)
                    {
                        Console.WriteLine(rate.values[position]);
                        tempRates.RemoveAt(i);
                    }
                }
                i = i + 1;
                return tempRates;
            }
            else if (ones == zeros && type == "o2") //kick out all zeros because o2
            {
                Console.WriteLine("Theyre equal removing all zeros! Postion {0}", position+1);
                foreach (var rate in rates)
                {
                    if (rate.values[position] == 0)
                    {
                        tempRates.RemoveAt(i);
                    }
                }
                i = i + 1;
                return tempRates;
            }
            else //kick out all ones because CO2 Scribber
            {
                foreach (var rate in rates)
                {
                    if (rate.values[position] == 1)
                    {
                        tempRates.RemoveAt(i);
                    }
                }
                return tempRates;
            }

        }
    }
}
