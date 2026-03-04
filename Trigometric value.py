import math


angle_deg = float(input("Enter an angle in degrees: "))


angle_rad = math.radians(angle_deg)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)


print(f"sin({angle_deg}) = {sin_val}")
print(f"cos({angle_deg}) = {cos_val}")


if math.isclose(cos_val, 0.0, abs_tol=1e-9):
    print