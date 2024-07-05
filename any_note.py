##List Comprehension
# Example  (expression for item in iterable if condition)

for i in range(2, num):
        if i % 2 == 0:
            continue
        if num % i != 0:
            p_list.append(i)

    # Remove numbers from p_list that are divisible by any number between 2 and themselves
    p_list = [number for number in p_list if all(number % i != 0 for i in range(2, number))]

#  p_kist 에 숫자 하나마다 if 절로 체크, all()은 true or false로 반환. all 안에 조건은 숫자가 특정 숫자로 나눠지지 않는 것을 True로 반환
# 그 숫자가 True로 반환되면 new p_list에 넣어짐

#---------------------------------------------------------------



## Using the * Operator to Unpack the Generator
print(*(n for n in range(1, 28)))