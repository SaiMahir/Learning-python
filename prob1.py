def display_primes(n=100):
    

    for num in range( 3 ,n+1):
      
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)

# Function call
display_primes(100)
