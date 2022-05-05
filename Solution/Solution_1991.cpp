#include <iostream>
using namespace std;

//2022-04-08 baekjoon1991 트리순회
//하나의 노드 정보를 선언
typedef struct node* TreeNode;
class node {
public:
	char key;
	TreeNode left,right;
	node() {
		key = NULL;
		left = NULL;
		right = NULL;
	}
	node(int k,TreeNode l,TreeNode r) {
		key = k;
		left = l;
		right = r;
	}
	~node() {
		delete left;
		delete right;
		//cout << "\n소멸자 호출" << endl;
		
	}
};

//전위순회
void preorder(TreeNode ptr) {
	if (ptr != NULL) {
		cout << ptr->key ;    //(1)먼저 자기 자신을 처리 
		preorder(ptr->left);  //(2)왼쪽 자식 방문
		preorder(ptr->right); //(3)오른쪽 자식 방문 

	}
}

//중위 순회
void inorder(TreeNode ptr) {
	if (ptr != NULL) {
		inorder(ptr->left);   //(1)왼쪽 자식 방문
		cout << ptr->key;    //(2)자기 자신을 처리
		inorder(ptr->right);  //(3)오른쪽 자식 방문
	}
	
}
//후위 순회
void postorder(TreeNode ptr) {
	if (ptr != NULL) {
		postorder(ptr->left); //(1)왼쪽 자식 방문
		postorder(ptr->right); //(2)오른쪽 자식 방문
		cout << ptr->key;    //(3)자기 자신을 처리
	}
	
}

void setNode(TreeNode root, char data1, char data2) {
	TreeNode leftNode = new node(data1,NULL,NULL);
	TreeNode rightNode = new node(data2, NULL, NULL);
	
	if (data1 != '.') {
		root->left = leftNode;
	}
	if (data2 != '.') {
		root->right = rightNode;
	}

}
//재귀를 이용한 탐색
TreeNode searchNode(TreeNode tree, char key) {
    if (tree != NULL) {
        if (tree->key == key) return tree;
        else {
            TreeNode temp = searchNode(tree->left, key);
            if (temp != NULL) return temp;
        }
        return searchNode(tree->right, key);
    }

    return NULL;
}

int main() {
	int n ;
	cin >> n;
	TreeNode tree = new node('A', NULL, NULL);

	char c1, c2, c3;
	for (int i = 0; i < n; i++) {
		cin >> c1>>c2>> c3;

		if (searchNode(tree, c1)) {
			setNode(searchNode(tree, c1), c2, c3);
		}
	}
	
	
	preorder(tree);
	cout << endl;
	inorder(tree);
	cout << endl;
	postorder(tree);
	delete tree;
	
}
