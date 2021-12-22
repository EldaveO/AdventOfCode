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
            var tempRates = new List<Rate>(rates);


            if (ones > zeros) //kick out zeros
            {
                Console.WriteLine("removing all zeros! index {0}");
                for (int i = tempRates.Count-1; i >= 0 ; i--)
                {
                    if (tempRates[i].values[position] == 0)
                    {
                        Console.WriteLine(tempRates[i].values[position]);
                        tempRates.RemoveAt(i); 
                    }
                }
                return tempRates;
            }
            else if (ones < zeros) //kick out ones
            {
                Console.WriteLine("removing all ones! index {0}");
                for (int i = tempRates.Count-1; i >= 0; i--)
                {
                    if (tempRates[i].values[position] == 1)
                    {
                        Console.WriteLine(tempRates[i].values[position]);
                        tempRates.RemoveAt(i);
                    }
                }
                return tempRates;
            }
            else if (ones == zeros && type == "o2") //kick out all zeros because o2
            {
                Console.WriteLine("Theyre equal removing all zeros! Postion {0}", position+1);
                for (int i = tempRates.Count-1; i >= 0; i--)
                {
                    if (tempRates[i].values[position] == 0)
                    {
                        Console.WriteLine(tempRates[i].values[position]);
                        tempRates.RemoveAt(i);
                    }
                }
                return tempRates;
            }
            else //kick out all ones because CO2 Scribber
            {
                Console.WriteLine("Theyre equal removing all ones! Postion {0}", position + 1);
                for (int i = tempRates.Count - 1; i >= 0; i--)
                {
                    if (tempRates[i].values[position] == 1)
                    {
                        Console.WriteLine(tempRates[i].values[position]);
                        tempRates.RemoveAt(i);
                    }
                }
                return tempRates;
            }

        }
    }
}
