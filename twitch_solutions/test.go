// add("A", 0)
// add("B", 1)
// add("D", 2)
// add("C", 2)
// add("Z", 0)
// Z, A, B, C, D​
package main

import (
	"errors"
	"fmt"
)

type (
	List struct {
		Head *ListNode
		Len  int
	}

	ListNode struct {
		Next *ListNode
		Prev *ListNode
		Val  string
	}
)

func (list *List) add(val string, place int) error {
	if place > list.Len {
		return errors.New("Can't insert to the current place")
	}
	list.Len++

	cur := list.Head
	if cur == nil {
		list.Head = &ListNode{nil, nil, val}
		return nil
	}
	for ; place > 1; place-- {
		cur = cur.Next
	}

	next := cur.Next
	cur.Next = &ListNode{next, cur, val}
	return nil
}

func printList(list *List) {
	cur := list.Head
	for cur != nil {
		fmt.Printf("%s ", cur.Val)
	}
	fmt.Println()
}

func main() {
	list := &List{}
	list.add("A", 0)
	list.add("B", 1)
	list.add("D", 2)
	list.add("C", 2)
	list.add("Z", 0)
	printList(list)
}
