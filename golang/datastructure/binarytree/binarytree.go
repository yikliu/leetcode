package binarytree

import (
	"golib/datastructure/comparable"
)

type BTNode struct {
	element interface{}
	left    *BTNode
	right   *BTNode
}

type BinaryTree struct {
	root *BTNode
	size int
}

func New() *BinaryTree {
	return &BinaryTree{root: nil, size: 0}
}

func (bt *BinaryTree) Insert(elem interface{}) {

	bt.root = bt.insert(bt.root, &BTNode{element: elem, left: nil, right: nil})
	bt.size += 1
}

func (bt *BinaryTree) Lookup(target interface{}) (*BTNode, bool) {
	return bt.lookup(bt.root, target)
}

//recursive insertion
func (bt *BinaryTree) insert(root *BTNode, pNewNode *BTNode) *BTNode {
	if root == nil {
		root = pNewNode
		return root
	}

	if comparable.Compare(root.element, pNewNode.element) < 0 {
		root.right = bt.insert(root.right, pNewNode)
	} else {
		root.left = bt.insert(root.left, pNewNode)
	}

	return root
}

func (bt *BinaryTree) lookup(node *BTNode, target interface{}) (*BTNode, bool) {
	if node == nil {
		return nil, false
	}

	if node.element == target {
		return node, true
	}

	if comparable.Compare(node.element, target) < 0 {
		return bt.lookup(node.right, target)
	} else {
		return bt.lookup(node.left, target)
	}
}
