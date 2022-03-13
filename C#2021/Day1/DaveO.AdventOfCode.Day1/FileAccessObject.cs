using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace DaveO.AdventOfCode.Day1
{
    public class FileAccessObject
    {
        public static void SaveText(string path, string value)
        {
            StreamWriter writer = new StreamWriter(path, true);
            try
            {
                writer.WriteLine(value);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                writer.Close();
            }


        }

        public static string[] GetText(string path)
        {
            //StreamReader reader = new StreamReader(path);
            string[] contents = null;
            try
            {
                contents = File.ReadAllLines(path);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            return contents;
        }
    }
}

