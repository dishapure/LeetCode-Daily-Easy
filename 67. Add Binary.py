a = "11"
b = "111"
carry = 0
result = ""

# make lengths equal by padding leading zeros
if len(a) < len(b):
    a = "0" * (len(b) - len(a)) + a
elif len(b) < len(a):
    b = "0" * (len(a) - len(b)) + b

# add bits from right to left
for i in range(len(a) - 1, -1, -1):
    a_bit = int(a[i])
    b_bit = int(b[i])
    total = a_bit + b_bit + carry

    if total == 0:
        result_bit = "0"
        carry = 0
    elif total == 1:
        result_bit = "1"
        carry = 0
    elif total == 2:
        result_bit = "0"
        carry = 1
    elif total == 3:
        result_bit = "1"
        carry = 1

    result = result_bit + result  # prepend because we go right → left

# handle final carry
if carry == 1:
    result = "1" + result

print(result)
