module DayOne

System.IO.File.ReadLines("./input.txt")
|> Seq.sumBy int
|> printfn "Frequency: %A"