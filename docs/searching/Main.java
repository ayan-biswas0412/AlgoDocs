package docs.searching;

import java.util.*;

public class Main{
    //Creating a linear search function
public static int LinearSearch(int[] arr, int n, int key){
    for(int i=0;i<n;i++){
        //comparing the element with the elemnents of the array 
        if(arr[i]==key){
         //returns the index of the element if the element is found
            return i;

        }
    }
    //if the element is not in the array then return -1;
    return -1;
}
    public static void main(String[] args){
    Scanner sc=new Scanner(System.in);        
    int n=sc.nextInt();
    int[] arra=new int[8];
    for(int i=0;i<n;i++){
        arra[i]=sc.nextInt();
    }
    int key=sc.nextInt();

    System.out.println(LinearSearch(arra, n, key));
    


    }
}