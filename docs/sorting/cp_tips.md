# Tips & TRICKS For Competitive Programing

## Sum from 0th position to nth position of a loop

```
int k = n * (n + 1) / 2;
\\ suppose n=4  than 4*(5)/2==>10  (1+2+3+4)
```

## Sort Array in Decreasing order

```
int main()
{
    vector<int> v{ 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
    //using greater function
    sort(v.begin(), v.end(), greater<int>());

    cout << "Sorted \n";
    for (auto x : v)
        cout << x << " ";

    return 0;
}
```

# Prime Number

```
bool isprime(int n)
{
    for(int i=2;i*i<=n;i++){
        if(n%i==0)
        return false;
    }
    return true;
}

```

# T-Prime(Number Divisible by three Numbers)

## To find T-Prime we have to call isprime function and insert the square of prime number in a set

```
for(int i=3;i<=1000000;i+=2)
    {
        if(isprime(i))
        {
           tprime.insert(i*i);
        }
    }
```

## Sum of all digits in the decimal representation of number x.

```
int S(int x)
{
    if (x < 0)return -1;
    ll s = 0;
    while(x)
    {
        s += x%10;
        x /= 10;
    }

    return s;
}
```

## Sort Function inline comapre function for pairs

```
inline bool cmp (const pair<int, int>&a, const pair<int, int>&b)
{
    if (a.first != b.first)
        return a.first > b.first;

    return a.second < b.second;
}
```
