namespace CodeRetreat.Console
{
    using System;
    using CodeRetreat.Model;

    public class Program
    {
        public static void Main(string[] args)
        {
            var dummy = new Dummy();
            var hello = dummy.Hello();

            Console.WriteLine(hello);

            Console.ReadLine();
        }
    }
}
