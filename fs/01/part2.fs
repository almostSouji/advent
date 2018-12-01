module PartTwo

let input = System.IO.File.ReadLines("./input.txt")
            |> Seq.toList
            |> List.map int

let rec solve (list :int List) (values :int List) (b :int) :int =
    // printfn "%A" (List.head values);
    match list with
    | [] -> printfn "%A" b;
            solve (input) (values) (b+1)
    | x::xs -> let y = x + List.head values in 
                if List.contains y values then y else solve (xs) (y :: values) (b)

solve input [0] 0
|> printfn "%A"