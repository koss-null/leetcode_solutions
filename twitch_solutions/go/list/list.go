package list

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type nodeToProcess struct {
	Node   *TreeNode
	Parent *TreeNode
}

func NewTree(data []interface{}) *TreeNode {
	if len(data) == 0 {
		return nil
	}
	var head = &TreeNode{}
	toProcess := make([]nodeToProcess, 0, len(data)/2)
	toProcess = append(toProcess, nodeToProcess{head, nil})

	for _, d := range data {
		cur := toProcess[0]
		toProcess = toProcess[1:]
		if value, converted := d.(int); converted {
			cur.Node.Val = value
			cur.Node.Left = &TreeNode{}
			cur.Node.Right = &TreeNode{}
			toProcess = append(
				toProcess,
				nodeToProcess{cur.Node.Left, cur.Node},
				nodeToProcess{cur.Node.Right, cur.Node},
			)
		} else { // null
			if cur.Parent.Left == cur.Node {
				cur.Parent.Left = nil
				continue
			}
			cur.Parent.Right = nil
		}
	}

	for i := range toProcess {
		if toProcess[i].Node == toProcess[i].Parent.Left {
			toProcess[i].Parent.Left = nil
		} else {
			toProcess[i].Parent.Right = nil
		}
	}

	return head
}
