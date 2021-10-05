# Red-Black tree

A red-black tree is a binary search tree with one extra bit of storage per node: its color, which can be either RED or BLACK. By constructing 
the node colors on any simple path from the root to a leaf, red-black tree ensures that no such path is more than twice as long as any other, 
so that red-black tree is approximately balanced.
A red-black tree is a binary search tree that satisfies the following RED-BLACK PROPERTIES:
    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf node(nil) is black.
    4. If a node is red, then both its children are black.
    5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

## Algorithm

```
ROTATIONS:  Changes the pointer structure through rotation, which is a local operation in a search tree that preserves the BINARY-SEARCH-TREE PROPERTY.

INSERTION:  Insert a new node at leaf position and color it as RED and then call the subroutine RB-INSERT-FIXUP to make arrangements to maintain the RED-BLACK PROPERTIES.

TRANSPLANT: It replaces the subtree rooted at a node with the subtree rooted at some other node.

DELETION:   Find the node, find its child nodes and delete the specific node, then call the subroutine RB-DELETE-FIXUP to make arrangements to maintain the RED-BLACK PROPERTIES.

```

## Pseudocode

```
Red-Black tree
    Node attributes
        Node   : x is an arbitrary node in the red-black tree
        x.key  : The data value stored in the node x
        x.color: The boolean attribute which stores the color of x
        x.p    : The pointer which point to the parent node of x
        x.left : The pointer which point to the left child node of x
        x.right: The pointer which point to the right child node of x
    Tree attributes:
        T      : T is a arbitrary red-black tree
        T.root : The root of the red-black tree T, which have always Black color
        T.nil  : It is a special node which have no parent and no data stored in it and always have Black color


    TREE-SEARCH(x,k)
        if x==T.nil or k==x.key
            return x
        if k < x.key
            return TREE-SEARCH(x.left,k)
        else
            return TREE-SEARCH(x.right,k)


    TREE-MINIMUM(T,x)
        while(x.left!=T.nil)
            x=x.left
        return x


    LEFT-ROTATE(T,x)
        y=x.right
        x.right=y.left
        if y.left!=T.nil
            y.left.p=x
        y.p=x.p
        if x.p==T.nil
            T.root=y
        elseif x==x.p.left
            x.p.left=y
        else
            x.p.right=y
        y.left=x
        x.p=y
    
    RIGHT-ROTATE(T,x)
        y=x.left
        x.left=y.right
        if y.right!=T.nil
            y.right.p=x
        y.p=x.p
        if x.p==T.nil
            T.root=y
        elseif x==x.p.left
            x.p.left=y
        else
            x.p.right=y
        y.right=x
        x.p=y


    RB-INSERT-FIXUP(T,z)
        while z.p.color==RED
            if z.p==z.p.p.left
                y=z.p.p.right
                if y.color==RED
                    z.p.color=BLACK
                    y.color=BLACK
                    z.p.p.color=RED
                    z=z.p.p
                else
                    if z==z.p.right
                    z=z.p
                    LEFT-ROTATE(T,z)
                z.p.color=BLACK
                z.p.p.color=RED
                RIGHT-ROTATE(T,z.p.p)
            else
                y=z.p.p.left
                if y.color==RED
                    z.p.color=BLACK
                    y.color=BLACK
                    z.p.p.color=RED
                    z=z.p.p
                else
                    if z==z.p.left
                    z=z.p
                    RIGHT-ROTATE(T,z)
                z.p.color=BLACK
                z.p.p.color=RED
                LEFT-ROTATE(T,z.p.p)
        T.root.color=BLACK


    RB-TRANSPLANT(T,u,v)
        if u.p==T.nil
            T.root=v
        elseif u==u.p.left
            u.p.left=v
        else
            u.p.right=v
        v.p=u.p


    RB-DELETE-FIXUP(T,x)
        while x!=T.root and x.color==BLACK
            if x==x.p.left
                w=x.p.right
                if w.color==RED
                    w.color=BLACK
                    x.p.color=RED
                    LEFT-ROTATE(T,x.p)
                    w=x.p.right
                if w.left.color==BLACK and w.right.color==BLACK
                    w.color=RED
                    x=x.p
                else
                    if w.right.color==BLACK
                        w.left.color=BLACK
                        w.color=RED
                        RIGHT-ROTATE(T,w)
                        w=x.p.right
                w.color=x.p.color
                x.p.color=BLACK
                w.right.color=BLACK
                LEFT-ROTATE(T,x.p)
                x=T.root
            else
                w=x.p.left
                if w.color==RED
                    w.color=BLACK
                    x.p.color=RED
                    RIGHT-ROTATE(T,x.p)
                    w=x.p.left
                if w.left.color==BLACK and w.right.color==BLACK
                    w.color=RED
                    x=x.p
                else
                    if w.left.color==BLACK
                        w.right.color=BLACK
                        w.color=RED
                        LEFT-ROTATE(T,w)
                        w=x.p.left
                    w.color=x.p.color
                    x.p.color=BLACK
                    w.left.color=BLACK
                    RIGHT-ROTATE(T,x.p)
                    x=T.root
        x.color=BLACK


    RB-INSERT(T,z)
        y=T.nil
        x.T.root
        while x!=T.nil
            y=x
            if z.key < x.key
                x=x.left
            else 
                x=x.right
        z.p=y
        if y==T.nil
            T.root=z
        elseif z.key < y.key
            y.left=z
        else
            y.right=z
        z.left=T.nil
        z.right=T.nil
        z.color=RED
        RB-INSERT-FIXUP(T,z)


    RB-DELETE(T,z)
        y=z
        y-original-color=y.color
        if z.left==T.nil
            x=z.right
            RB-TRANSPLANT(T,z,z.right)
        elseif z.right==T.nil
            x=z.left
            RB-TRANSPLANT(T,z,z.left)
        else
            y=TREE-MINIMUM(z.right)
            y-original-color=y.color
            x=y.right
            if y.p==z
                x.p=y
            else
                RB-TRANSPLANT(T,y,y.right)
                y.right=z.right
                y.right.p=y
            RB-TRANSPLANT(T,z,y)
            y.left=z.left
            y.left.p=y
            y.color=z.color
        if y-original-color==BLACK
            RB-DELETE-FIXUP(T,x)

```
## Code

### C++ Implementation

```cpp
#include<iostream>
#include<iomanip>
using namespace std;
enum color{RED,BLACK};
class Node
{
public:
    int data;
    bool color;
    Node* parent;
    Node* left;
    Node* right;
    Node(int el,bool col,Node* p,Node* l,Node* r)
    {
        data=el;
        color=col;
        parent=p;
        left=l;
        right=r;
    }
};
class Rbtree
{
private:
    Node* root;
    Node* nil;
    void rotate_left(Node* temp)
    {
        Node* right_child=temp->right;
        temp->right=right_child->left;
        if(right_child->left!=nil)
        {
            right_child->left->parent=temp;
        }
        right_child->parent=temp->parent;
        if(temp->parent==nil)
        {
            root=right_child;
        }
        else if(temp==temp->parent->left)
        {
            temp->parent->left=right_child;
        }
        else
        {
            temp->parent->right=right_child;
        }
        right_child->left=temp;
        temp->parent=right_child;
    }
    void rotate_right(Node* temp)
    {
        Node* left_child=temp->left;
        temp->left=left_child->right;
        if(left_child->right!=nil)
        {
            left_child->right->parent=temp;
        }
        left_child->parent=temp->parent;
        if(temp->parent==nil)
        {
            root=left_child;
        }
        else if(temp==temp->parent->left)
        {
            temp->parent->left=left_child;
        }
        else
        {
            temp->parent->right=left_child;
        }
        left_child->right=temp;
        temp->parent=left_child;
    }
    void rb_insert_fixup(Node* temp)
    {
        while(temp->parent->color==RED)
        {
            if(temp->parent==temp->parent->parent->left)
            {
                Node* uncle=temp->parent->parent->right;
                if(uncle->color==RED)
                {
                    temp->parent->color=BLACK;
                    uncle->color=BLACK;
                    temp->parent->parent->color=RED;
                    temp=temp->parent->parent;
                }
                else
                {
                    if(temp==temp->parent->right)
                    {
                        temp=temp->parent;
                        rotate_left(temp);
                    }
                    temp->parent->color=BLACK;
                    temp->parent->parent->color=RED;
                    rotate_right(temp->parent->parent);
                }
            }
            else
            {
                Node* uncle=temp->parent->parent->left;
                if(uncle->color==RED)
                {
                    temp->parent->color=BLACK;
                    uncle->color=BLACK;
                    temp->parent->parent->color=RED;
                    temp=temp->parent->parent;
                }
                else
                {
                    if(temp==temp->parent->left)
                    {
                        temp=temp->parent;
                        rotate_right(temp);
                    }
                    temp->parent->color=BLACK;
                    temp->parent->parent->color=RED;
                    rotate_left(temp->parent->parent);
                }
            }
        }
        root->color=BLACK;
    }
    Node* rb_insert_node(Node* temp,Node* par,int el)
    {
        if(temp==nil)
        {
            temp=new Node(el,RED,par,nil,nil);
            if(par==nil)
            {
                root=temp;
            }
            if(el < par->data)
            {
                par->left=temp;
            }
            else
            {
                par->right=temp;
            }
        }
        else
        {
            if(el < temp->data)
            {
                return(rb_insert_node(temp->left,temp,el));
            }
            else
            {
                return (rb_insert_node(temp->right,temp,el));
            }
        }
        return temp;
    }
    Node* rb_find_node(Node* temp,int el)
    {
        if(temp==nil)
        {
            return nil;
        }
        if(el < temp->data)
        {
            return (rb_find_node(temp->left,el));
        }
        else if(el > temp->data)
        {
            return (rb_find_node(temp->right,el));
        }
        else
        {
            return temp;
        }
    }
    Node* rb_find_min(Node* temp)
    {
        Node* ptr;
        while(temp!=nil)
        {
            ptr=temp;
            temp=temp->left;
        }
        return ptr;
    }
    
    void rb_transplant(Node* u,Node* v)
    {
        if(u->parent==nil)
        {
            root=v;
        }
        else if(u==u->parent->left)
        {
            u->parent->left=v;
        }
        else
        {
            u->parent->right=v;
        }
        v->parent=u->parent;
    }
    void rb_delete_fixup(Node* temp)
    {
        while(temp!=root && temp->color==BLACK)
        {
            if(temp==temp->parent->left)
            {
                Node* sibling=temp->parent->right;
                if(sibling->color==RED)
                {
                    sibling->color=BLACK;
                    temp->parent->color=RED;
                    rotate_left(temp->parent);
                    sibling=temp->parent->right;
                }
                if(sibling->left->color==BLACK && sibling->right->color==BLACK)
                {
                    sibling->color=RED;
                    temp=temp->parent;
                }
                else
                {
                    if(sibling->right->color==BLACK)
                    {
                        sibling->left->color=BLACK;
                        sibling->color=RED;
                        rotate_right(sibling);
                        sibling=temp->parent->right;
                    }
                    sibling->color=temp->parent->color;
                    temp->parent->color=BLACK;
                    sibling->right->color=BLACK;
                    rotate_left(temp->parent);
                    temp=root;
                }
            }
            else
            {
                Node* sibling=temp->parent->left;
                if(sibling->color==RED)
                {
                    sibling->color=BLACK;
                    temp->parent->color=RED;
                    rotate_right(temp->parent);
                    sibling=temp->parent->left;
                }
                if(sibling->left->color==BLACK && sibling->right->color==BLACK)
                {
                    sibling->color=RED;
                    temp=temp->parent;
                }
                else
                {
                    if(sibling->left->color==BLACK)
                    {
                        sibling->right->color=BLACK;
                        sibling->color=RED;
                        rotate_left(sibling);
                        sibling=temp->parent->left;
                    }
                    sibling->color=temp->parent->color;
                    temp->parent->color=BLACK;
                    sibling->left->color=BLACK;
                    rotate_right(temp->parent);
                    temp=root;
                }
            }
        }
        temp->color=BLACK;
    }
    void rb_delete_node(Node* temp)
    {
        Node* y=temp;
        Node* x;
        int y_original_color=y->color;
        if(temp->left==nil)
        {
            x=temp->right;
            rb_transplant(temp,temp->right);
        }
        else if(temp->right==nil)
        {
            x=temp->left;
            rb_transplant(temp,temp->left);
        }
        else
        {
            y=rb_find_min(temp->right);
            y_original_color=y->color;
            x=y->right;
            if(y->parent==temp)
            {
                x->parent=y;
            }
            else
            {
                rb_transplant(y,y->right);
                y->right=temp->right;
                y->right->parent=y;
            }
            rb_transplant(temp,y);
            y->left=temp->left;
            y->left->parent=y;
            y->color=temp->color;
        }
        if(y_original_color==BLACK)
        {
            rb_delete_fixup(x);
        }
    }
    
    void rb_show_data(Node* temp)
    {
        if(temp==nil || temp==NULL)
        {
            return;
        }
        else
        {
            rb_show_data(temp->left);
            cout<<setw(5)<<temp->data<<setw(10)<<temp->color<<endl;
            rb_show_data(temp->right);
        }
    }
public:
    Rbtree()
    {
        nil=new Node(-1,BLACK,NULL,NULL,NULL);      //the main master trick
        root=nil;
    }
    void insert_node(int el)
    {
        Node* temp=rb_insert_node(root,nil,el);
        rb_insert_fixup(temp);
    }
    void delete_node(int el)
    {
        Node* temp=rb_find_node(root,el);
        if(temp==nil)
        {
            return;
        }
        else
        {
            rb_delete_node(temp);
        }
    }
    void show_data()
    {
        cout<<"Inorder walk"<<endl;
        cout<<"   "<<"Data"<<"     "<<"Color"<<endl;
        rb_show_data(root);
    }
    void show_root_data()
    {
        cout<<"The informations of the Root node is"<<endl;
        cout<<"   "<<"Data"<<"     "<<"Color"<<endl;
        cout<<setw(5)<<root->data<<setw(10)<<root->color<<endl;
    }
};
int main()
{
    Rbtree rbt;

    rbt.insert_node(9);
    rbt.insert_node(7);
    rbt.insert_node(11);
    rbt.insert_node(6);
    rbt.insert_node(15);
    rbt.insert_node(8);
    rbt.insert_node(18);
    rbt.insert_node(16);
    rbt.insert_node(17);
    rbt.insert_node(5);
    rbt.insert_node(4);
    rbt.insert_node(23);
    rbt.insert_node(45);
    rbt.insert_node(50);
    rbt.insert_node(70);
    rbt.insert_node(115);

    rbt.show_data();
    rbt.show_root_data();

    rbt.delete_node(9);
    rbt.show_data();
    rbt.show_root_data();
    return 0;
}
```

## Time Complexity

The time complexity of data insertion and deletion in Red-Black tree is O(log N), where N is the number of keys stored.

## Space Complexity

The space complexity of Red-Black tree is O(N), where N is the number of keys stored.

## Sources
    
- [Book-Introduction to Algorithms by CLRS](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)