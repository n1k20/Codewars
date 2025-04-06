def int32_to_ip(int32: int) -> str:
    number2 = bin(int32)[2:].zfill(32)
    return f'{int(number2[:8], 2)}.{int(number2[8:16], 2)}.{int(number2[16:24], 2)}.{int(number2[24:32], 2)}'
print(int32_to_ip(int32=2149583361))