using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DaveO.AdventOfCode.Day3
{
    public class Rate
    {
        //fields
        const string path = @"C:\Users\davido\Documents\DaveCode\AdventOfCode\Day3\Data.csv";

        public int[] values;

        //constructors
        public Rate() { }

        public Rate(int[] values)
        {
            this.values = values;
        }

        //properties

        //methods
        public static List<Rate> GetRates()
        {
            string[] records = FileAccessObject.GetText(path);
            string[] rate = null;
            Rate rat = null;
            List<Rate> rates = new List<Rate>();

            foreach (string record in records)
            {
                rate = record.Split(char.Parse(","));
                rat = new Rate(Array.ConvertAll(rate, int.Parse));
                rates.Add(rat);
            }
            return rates;
        }

        public static bool IsOne(int value)
        {
            if (value == 1)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
