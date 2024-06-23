def find_pairs(target_product, target_sum):
    for p in range(1, target_product + 1):
        if target_product % p == 0:  # p가 target_product의 약수인 경우
            q = target_product // p
            if p + q < target_sum:
                print(f"p = {p}, q = {q}")

# 입력 받기
product = int(input("p*q의 곱을 입력하세요: "))
sum_limit = int(input("p+q의 합의 최댓값을 입력하세요: "))

# 함수 호출
find_pairs(product, sum_limit)
