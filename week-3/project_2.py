def quartic_roots(A, B, C, D, E):
    # Calculate intermediate coefficients
    p = (8*A*C - 3*B**2) / (8*A**2)
    q = (B**3 - 4*A*B*C + 8*A**2*D) / (8*A**3)
    r = (-3*B**4 + 256*A**3*E - 64*A**2*B*D + 16*A*B**2*C) / (256*A**4)

    # Solve the depressed quartic equation: y^4 + py^2 + qy + r = 0
    # We can use the quadratic formula for y^2
    discriminant = q**2 - 4*p**3
    sqrt_discriminant = discriminant**0.5

    y1 = (-q + sqrt_discriminant) / 2
    y2 = (-q - sqrt_discriminant) / 2

    # Calculate the roots of the original quartic equation
    root1 = (y1 - B) / (4*A)
    root2 = (-y1 - B) / (4*A)
    root3 = (y2 - B) / (4*A)
    root4 = (-y2 - B) / (4*A)

    return [root1, root2, root3, root4]

A =int(input("Value of A "))
B =int(input("Value of B "))
C =int(input("Value of C "))
D =int(input("Value of D "))
E =int(input("Value of E "))

roots = quartic_roots(A, B, C, D, E)
print("Roots:", roots)
