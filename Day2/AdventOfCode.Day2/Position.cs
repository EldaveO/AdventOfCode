using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode.Day2
{
    class Position
    {
        // fields
        public string position; 
        public int value;
        const string path = @"C:\Users\davido\Documents\DaveCode\AdventOfCode\Day2\Data.csv";

        // constructors
        public Position() { }
        public Position(string position, int value) 
        {
            this.position = position;
            this.value = value;
        }

        // properties

        // methods
        public static List<Position> GetPostions()
        {
            string[] records = FileAccessObject.GetText(path);
            string[] position = null;
            Position pos = null;
            List<Position> positions = new List<Position>();

            foreach (string record in records)
            {
                position = record.Split(char.Parse(","));
                pos = new Position(position[0], int.Parse(position[1]));
                positions.Add(pos);
            }
            return positions;
        }
    }
}
