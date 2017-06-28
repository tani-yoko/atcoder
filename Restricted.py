#問題文
#二つの整数 A, B が入力されます。A+B の値を出力してください。

#ただし、A+B が 10 以上の場合は、代わりに error と出力してください。

#制約
#A, B は整数である。
#1≤A,B≤9

A,B=map(int,input("数字は?").split())
print("error" if A+B>9 else A+B)
