cd ./../module7

./ex00/parameter_matching.py
echo "Hello" | ./ex00/parameter_matching.py "Hello"
echo "Bonjour" | ./ex00/parameter_matching.py "Hello"
echo ""
./ex01/count_it.py 
./ex01/count_it.py "1" "22" "333" "4444" 
echo ""
./ex02/string_are_arrays.py 
./ex02/string_are_arrays.py "catzieszero"
./ex02/string_are_arrays.py "catiesero"
echo ""
./ex03/append_it.py 
./ex03/append_it.py "parallelism" "egoism" "human" 
echo ""
./ex04/free_range.py
./ex04/free_range.py "10" "12"
./ex04/free_range.py "12" "10"
