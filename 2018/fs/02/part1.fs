module PartOne

let input = System.IO.File.ReadLines("./input.txt")
            |> Seq.toList
            |> List.map Seq.toList


let checkWord (word: char list) : bool * bool =
    let folder (tw, th) char =
        let c = List.filter (fun e -> e = char) word
        match List.length c with
        | 2 -> (true, th)
        | 3 -> (tw, true)   
        | _ -> (tw, th)


    List.fold folder (false, false) word

let iterate (wordList: char list list) =
    let folder (tws, ths) word = 
        let (a,b) = checkWord word
        ((if a then tws + 1 else tws), (if b then ths + 1 else ths))
    
    List.fold folder (0,0) wordList

let (a, b) = iterate input

printfn "Twos: %A" a
printfn "Threes: %A" b
printfn "Checksum: %A" (a * b)