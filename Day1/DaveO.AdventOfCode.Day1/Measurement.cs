using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DaveO.AdventOfCode.Day1
{
    public class Measurement
    {
        //fields
        private int _value;
        private const string _path = @"C:\Users\davido\Documents\GitHub\AdventOfCode\Day1\DaveO.AdventOfCode.Day1\Data.csv";

        //constructors
        public Measurement() { }

        public Measurement(int value)
        {
            this.Value = value;
        }

        //propeties
        public int Value
        {
            get { return _value; }
            set { _value = value; }
        }

        //methods
        public static List<Measurement> GetMeasurements()
        {
            string[] records = FileAccessObject.GetText(_path);
            string[] measurement = null;
            Measurement measure = null;
            List<Measurement> measurements = new List<Measurement>();

            foreach (string record in records)
            {
                measurement = record.Split(char.Parse(","));
                measure = new Measurement(int.Parse(measurement[0]));              
                measurements.Add(measure);
            }
            return measurements;
        }
    }
}
