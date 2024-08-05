def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f"{i}{j}"

    return result
for number in range(3, 21):
    password = generate_password(number)
    print(f"{number} - {password}")


