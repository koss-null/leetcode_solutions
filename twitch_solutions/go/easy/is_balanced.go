package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type NodeNLvl struct {
	Node   *TreeNode
	Height int
}

var heightMap map[*TreeNode]int

func cleanUp() {
	heightMap = make(map[*TreeNode]int)
}

func height(node *TreeNode) int {
	if node == nil {
		return 0
	}
	if val, ok := heightMap[node]; ok {
		return val
	}
	height := 1 + int(math.Max(float64(height(node.Left)), float64(height(node.Right))))
	heightMap[node] = height
	return height
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		cleanUp()
		return true
	}
	if int(math.Abs(float64(height(root.Left)-height(root.Right)))) > 1 {
		cleanUp()
		return false
	}
	if root.Left != nil {
		if !isBalanced(root.Left) {
			cleanUp()
			return false
		}
	}
	if root.Right != nil {
		if !isBalanced(root.Right) {
			cleanUp()
			return false
		}
	}

	cleanUp()
	return true
}
