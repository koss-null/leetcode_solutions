package main

import "fmt"
import "strings"
import "encoding/json"
import "io/ioutil"

type Test struct {
    Input string `json:"input"`
    Output string `json:"output"`
}

func main() {
    var a strings.Builder
    a.Grow(1000 * 1000 * 10)
    for i := 0; i < 1000 * 1000 * 10; i++ {
       fmt.Fprintf(&a, "%d ", i)
    }
    as := a.String()
    var b strings.Builder
    b.Grow(20 * 1000 * 1000)
    fmt.Fprintf(&b, "%s\n%s", as, as)
    t := Test{Input: b.String(), Output: "4999999.5"}

    file, _ := json.Marshal(t)
    err := ioutil.WriteFile("test/test_large_go", file, 0666)
    if err != nil {
        fmt.Println(err.Error())
    }
}