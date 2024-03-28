def cubic_roots(A, B, C, D):
    # Calculate intermediate coefficients
    p = (3*A*C - B**2) / (3*A**2)
    q = (2*B**3 - 9*A*B*C + 27*A**2*D) / (27*A**3)

    # Calculate discriminant
    discriminant = q**2 / 4 + p**3 / 27

    if discriminant > 0:
        # Three distinct real roots
        root1 = (-q/2 + discriminant**0.5) ** (1/3) - (q/2 - discriminant**0.5) ** (1/3) - B / (3*A)
        return [root1]
    elif discriminant == 0:
        # One real root (multiple root)
        root1 = -q/2 ** (1/3) - B / (3*A)
        return [root1]
    else:
        # Complex roots
        r = ((-q/2) ** 2 + (discriminant)**0.5) ** (1/3)
        theta = 2 * 3.14159 / 3
        root1 = r * (complex(1, 0) * (1/2) + complex(0, 1) * (3**0.5)/2)
        root2 = r * (complex(1, 0) * (1/2) - complex(0, 1) * (3**0.5)/2)
        root3 = -(root1 + root2) - B / (3*A)
        return [root1, root2, root3]

A =int(input("Value of A "))
B =int(input("Value of B "))
C =int(input("Value of C "))
D =int(input("Value of D "))

roots = cubic_roots(A, B, C, D)
print("Roots:", roots)
