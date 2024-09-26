package main

import (
	"math"
)

func ceasar_cypher(str string, key int) string {
	res := ""
	for i := 0; i < len(str); i++ {
		letter := str[i]
		var asci float64 = float64(letter) - 96.0 + float64(key)
		asci = math.Mod(asci, 27) + 96
		res += string(rune(asci))
	}
	return res

}
func rev_ceasar_cypher(str string, key int) string {
	res := ""
	for i := 0; i < len(str); i++ {
		letter := str[i]
		var asci float64 = float64(letter) - 96.0 - float64(key)
		asci = math.Mod(asci, 27) + 96
		res += string(rune(asci))
	}
	return res

}
