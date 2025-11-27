cd ./../module2
echo 0 | ./ex00/iszero.py
echo 1 | ./ex00/iszero.py

echo 1 | ./ex01/isneg.py
echo 0 | ./ex01/isneg.py
echo -1 | ./ex01/isneg.py

echo "Python is awesome" | ./ex02/password.py
echo "Python is not awesome" | ./ex02/password.py

echo "1\n2" | ./ex03/mult.py
echo "-1\n2" | ./ex03/mult.py
echo "-1\n-2" | ./ex03/mult.py
echo "0\n2" | ./ex03/mult.py
