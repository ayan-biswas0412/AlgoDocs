# Binary Search

Binary search is recursive algorithm the works with a sorted array, it starts of the middle of the array, if the current value is less than target then its at the left of the array, and if it is bigger then is at the right.

## Algorithm

```
Step 1 − Get the midpoint of your array
Step 2 − If your target is in the midpoint return it
Step 3 − If the value in the midpoint is lower than your target, use the the midpoint as high
Step 4 − If the value in the midpoint is greater than your target, use the midpoint as low
```

## Pseudocode

```
procedure binary_search 
    array : list
    low   : lower bound 
    high  : higher bound 
    target: number we are searching 
  
    if high >= low

        mid = floor((high + low) / 2)

        if array[mid] == target
            return mid
        else if array[mid] > target
            return binary_search(array, low, mid - 1, target)
        else
            return binary_search(array, mid + 1, high, target)
        end if

    end if
end procedure
```

## Code

### C Implementation
```C
#include<stdio.h>
#include<stdlib.h>

struct tree
{
    int data;
    struct tree *left;
    struct tree *right;
};
typedef struct tree TREE;

TREE * insert(TREE *,int );
void inorder(TREE *);
void preorder(TREE *);
void postorder(TREE *);
TREE * Delete(TREE *,int );
void printIndegreeofrootnode();
void printOutdegreeofrootnode();
void printAddressofrootnode(TREE *);
void minimumvaluefromtree(TREE *);

int main()
{
    TREE *root = NULL;
    int choice,ch,data;
   while(1)
    {
        printf("MENU\n");
        printf("1-Insert into BST\n2-Inorder\n3-Preorder\n4-Postorder\n5-Delete\n6-Otherfunctions\n7-Exit\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1: printf("Enter the item to insert\n");
                    scanf("%d",&data);
                    root = insert(root,data);
                    break;
            case 2: if(root == NULL)
                    printf("Empty Tree\n");
                    else
                    {
                        printf("Inorder traversal is\n");
                        inorder(root);
                    }
                    break;
            case 3: if(root == NULL)
                    printf("Empty Tree\n");
                    else
                    {
                        printf("Preorder traversal is\n");
                        preorder(root);
                    }
                    break;
            case 4: if(root == NULL)
                    printf("Empty Tree\n");
                    else
                    {
                        printf("Postorder traversal is\n");
                        postorder(root);
                    }
                    break;
            case 5: printf("Enter the item to delete\n");
                    scanf("%d",&data);
                    root = Delete(root,data);
                    break;
            case 6: printf("1-print in-degree of root node\n2-print out-degree of root node\n3-print address of root node\n4-minimum value of tree\n");
                    scanf("%d",&ch);
                    if(ch==1)
                        printIndegreeofrootnode();
                    else if(ch==2)
                        printOutdegreeofrootnode();
                    else if(ch==3)
                        printAddressofrootnode(root);
                    else if(ch==4)
                        minimumvaluefromtree(root);
                    break;
            case 7:exit(0);
        }
    }
    return 0;
}

TREE * insert(TREE * root,int data)
{
    TREE *newnode;
    newnode=(TREE *)malloc(sizeof(TREE));
    if(newnode==NULL)
    {
        printf("Memory allocation failed\n");
        return root;
    }
  
    newnode->data=data;
    newnode->left=NULL;
    newnode->right=NULL;

    if(root==NULL)
    {
        printf("Root inserted successfully\n");
        return newnode;
    }

    TREE *curr,*parent;
    curr=root;
    parent=NULL;
    while(curr!=NULL)
    {
        parent=curr;
        if(newnode->data<curr->data)
            curr=curr->left;
        else
            curr=curr->right;
    }
    if(newnode->data<parent->data)
        parent->left=newnode;
    else
        parent->right=newnode;
    printf("Root inserted successfully\n");
    return root;
}

void inorder(TREE *root)
{
    if(root!=NULL)
    {
        inorder(root->left);
        printf("%d\t",root->data);
        inorder(root->right);
    }
}

void preorder(TREE *root)
{
    if(root!=NULL)
    {
        printf("%d\t",root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(TREE *root)
{
    if(root!=NULL)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d\t",root->data);
    }
}
TREE * Delete(TREE *root,int data)
{
    if(root==NULL)
    {
        printf("Tree is empty\n");
        return root;
    }
    TREE *curr,*par;//par=parent
    par=NULL;
    curr=root;
    while(curr!=NULL && data!=curr->data)
    {
        par=curr;
        if(data<curr->data)
            curr=curr->left;
        else
            curr=curr->right;
    }
    if(curr==NULL)
    {
        printf("Item not found\n");
        return root;
    }
    TREE *p,*succ;
    if(curr->left==NULL)
        p=curr->right;
    else if(curr->right==NULL)
        p=curr->left;
    else
    {
        succ=curr->right;
        while(succ->left!=NULL)
            succ=succ->left;
        succ->left=curr->left;
        p=curr->right;
    }
    if(par==NULL)
    {
        free(curr);
        return p;
    }
    if(curr==par->left)
        par->left=p;
    else
        par->right=p;
    free(curr);
    return root;
}

void printIndegreeofrootnode()
{
    printf("The in-degree of root node is 0\n");
}

void printOutdegreeofrootnode()
{
    printf("The Out-degree of root node is 2\n");
}

void printAddressofrootnode(TREE *root)
{
        printf("Address of root node is %d\n",&root);
}

void minimumvaluefromtree(TREE *root)
{
    TREE *temp;
    temp=(TREE *)malloc(sizeof(TREE));
    if(root==NULL)
    {
        printf("Tree empty\n");
    }
    temp=root;
    while(temp->left!=NULL)
        temp=temp->left;
    printf("Minimum value is %d\n",temp->data);
    free(temp);
}
```


### C++ Implementation

```C++
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
  
        // If the element is present at the middle
        // itself
        if (arr[mid] == x)
            return mid;
  
        // If element is smaller than mid, then
        // it can only be present in left subarray
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
  
        // Else the element can only be present
        // in right subarray
        return binarySearch(arr, mid + 1, r, x);
    }
  
    // We reach here when element is not
    // present in array
    return -1;
}
```

### Python Implementation

```python
def binary_search(array, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            return binary_search(array, low, mid - 1, target)
        else:
            return binary_search(array, mid + 1, high, target)
```
### Golang Implementation
```golang
func binarySearch(needle int, haystack []int) bool {

	low := 0
	high := len(haystack) - 1

	for low <= high{
		median := (low + high) / 2

		if haystack[median] < needle {
			low = median + 1
		}else{
			high = median - 1
		}
	}

	if low == len(haystack) || haystack[low] != needle {
		return false
	}

	return true
}
```
## Time Complexity

The time complexity of the above algorithm is O(logN).

## Space Complexity

The algorithm runs in constant space O(1).

## Sources
    
- [Binary Search - Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [Binary Search - geekforgeeks](https://www.geeksforgeeks.org/binary-search/)
