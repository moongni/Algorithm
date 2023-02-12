def find_cycle(mole: int, deno: int) -> bool:
    iter = 0

    while mole > 0:

        if iter > deno + 1:
            return True
        
        mole = (mole % deno) * 10
        iter += 1
    
    return False