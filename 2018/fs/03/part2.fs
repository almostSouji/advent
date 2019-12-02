module PartTwo

let input = System.IO.File.ReadLines("./input.txt")
            |> Seq.toList
            |> List.map Seq.toList

let compare (l1 : 'a list) (l2 : 'a list) =
    let (common, unique) = 
        List.zip l1 l2 
        |> List.partition (fun (a,b) -> a = b)

    if List.length unique = 1 then List.map (fun (a,_) -> a) common else []

let solve (lines : 'a list list) = 
    lines
    |> List.collect (fun line -> List.map (fun lin -> compare lin line)lines)
    |> List.concat

solve input
|> List.toArray
|> System.String
|> printfn "The right ID is: %A"
