module PartTwo
let input = System.IO.File.ReadLines("./input.txt")
            |> Seq.toList
            |> List.map int

let rec solve (list :int List) (values :int Set) (cFrequency :int) :int =
    match list with
    | [] -> solve (input) (values) (cFrequency)
    | x::xs -> let y = x + cFrequency in 
                if Set.contains y values then y else solve (xs) (Set.add y values) (y)

solve input (Set.add 0 Set.empty) 0
    |> printfn "%A"
