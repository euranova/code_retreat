namespace CodeRetreat
{
  using System;

  public class Dummy
  {

    public string Hello()
    {
      return "Hello World!";
    }

    public static void Main(string[] args)
    {
      Console.WriteLine(new Dummy().Hello());
    }

  }

}
