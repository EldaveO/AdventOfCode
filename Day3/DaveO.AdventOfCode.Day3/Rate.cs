using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DaveO.AdventOfCode.Day3
{
    class Rate
    {
        //fields
        const string path = @"C:\Users\davido\Documents\DaveCode\AdventOfCode\Day3\Data.csv";

        public int value1;
        public int value2;
        public int value3;
        public int value4;
        public int value5;
        public int value6;
        public int value7;
        public int value8;
        public int value9;
        public int value10;
        public int value11;
        public int value12;

        //constructors
        public Rate() { }
        public Rate(int value1, int value2, int value3, int value4, int value5, int value6, int value7, int value8, int value9, int value10, int value11, int value12)
        {
            this.value1 = value1;
            this.value2 = value2;
            this.value3 = value3;
            this.value4 = value4;
            this.value5 = value5;
            this.value6 = value6;
            this.value7 = value7;
            this.value8 = value8;
            this.value9 = value9;
            this.value10 = value10;
            this.value11 = value11;
            this.value12 = value12;
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
                rat = new Rate(int.Parse(rate[0]), int.Parse(rate[1]), int.Parse(rate[2]), int.Parse(rate[3]),
                                int.Parse(rate[4]), int.Parse(rate[5]), int.Parse(rate[6]), int.Parse(rate[7]),
                                int.Parse(rate[8]), int.Parse(rate[9]), int.Parse(rate[10]), int.Parse(rate[11]));
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
