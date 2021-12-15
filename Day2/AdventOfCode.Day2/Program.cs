using System;
using System.Collections.Generic;

namespace AdventOfCode.Day2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var records = Position.GetPostions();

            int forward = 0;
            int depth = 0;

            foreach (var position in records)
            {
                Console.WriteLine("{0}, {1}", position.position, position.value);

                switch (position.position)
                {
                    case "forward":
                        forward = position.value + forward;
                        break;
                    case "up":
                        depth = depth - position.value;
                        break;
                    case "down":
                        depth = depth + position.value;
                        break;
                }
            }
            Console.WriteLine("final forward position: {0}, final depth: {1}", forward, depth);
            Console.WriteLine(forward * depth);
            Console.ReadLine();
        }
    }
}
