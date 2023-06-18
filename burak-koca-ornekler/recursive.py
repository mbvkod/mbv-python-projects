def fact(num):
    if num > 1:
        result = fact(num - 1) * num
        print(result)
        return result
    else:
        return 1


fact(5)

# fact(5) = fact(4) * 5
# fact(4) = fact(3) * 4
# fact(3) = fact(2) * 3
# fact(2) = fact(1) * 2
# fact(1) = 1


# fact(5) = 120
# fact(4) = 24
# fact(3) = 6
# fact(2) = 2
# fact(1) = 1



