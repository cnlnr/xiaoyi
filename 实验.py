def calculate_stats(
        numbers,  # 位置参数
        **kwargs  # 可变关键字参数
    ) -> float:

    result = 0
    if operation == "sum":
        result = sum(numbers, *args)
    elif operation == "avg":
        result = sum(numbers, *args) / (len(numbers) + len(args))
    return round(result, precision)