# No pemdas
# (((((a+13)*b/c)+d+12)*e)-f-11+g)*h/j
# Pemdas
# a+13*b/c+d+12*e-f-11+g*h/j
for a in range(1,10):
    for b in range(1,10):
        if b == a:
            continue
        for c in range(1,10):
            if c == a or c == b:
                continue
            for d in range(1,10):
                if d == a or d == b or d == c:
                    continue
                for e in range(1,10):
                    if e == a or e == b or e == c or e == d:
                        continue
                    for f in range(1,10):
                        if f == a or f == b or f == c or f == d or f == e:
                            continue
                        for g in range(1,10):
                            if g == a or g == b or g == c or g == d or g == e or g == f:
                                continue
                            for h in range(1,10):
                                if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                    continue
                                for j in range(1,10):
                                    if j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h:
                                        continue
                                    no_pemdas = (((((a+13)*b/c)+d+12)*e)-f-11+g)*h/j
                                    pemdas = a+13*b/c+d+12*e-f-11+g*h/j
                                    if no_pemdas == 76 or pemdas == 76:
                                        print("Solution Found!")
                                        print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, j={j}")
                                        print("Order Of Operations: " + ("Sequential" if no_pemdas == 76 else "Pemdas"))