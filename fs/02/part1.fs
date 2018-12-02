module PartOne

let input = System.IO.File.ReadLines("./input.txt")
            |> Seq.toList
            |> List.map Seq.toList

let rec checkWord (word: char list) (two:bool, three:bool): bool*bool=
    match word with
    | [] -> (two, three)
    | x::xs -> let (c, d) = List.partition (fun e -> e = x) word
               match List.length c with
               | 2 -> checkWord d (true, three)
               | 3 -> checkWord d (two, true)   
               |_ -> checkWord xs (two, three)

let rec iterate (list: char list list) (twos: int, threes: int) :int*int = 
 match list with
 | [] -> (twos, threes)
 | x::xs -> let (a, b) = checkWord x (false, false)
            iterate xs ((if a then twos + 1 else twos), (if b then threes + 1 else threes))

let (a, b) = iterate input (0, 0)

printfn "Twos: %A" a
printfn "Threes: %A" b
printfn "Checksum: %A" (a * b)