import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        #print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(0.001)
        f *= i
    #print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 4),
        factorial("C", 8),
        factorial("D", 16),
        factorial("E", 32),
        factorial("F", 64),
    )
    print(L[0])
    print(L[1])
    print(L[2])
    print(L[3])
    print(L[4])
    print(L[5])

asyncio.run(main())