def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Las cadenas DNA no tienen la misma longitud.")

    return sum(1 for i in range(len(strand_a)) if strand_a[i] != strand_b[i])
    
