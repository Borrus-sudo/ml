import pandas as pd
import numpy as np
import sklearn as sc 
def rand_dat_gen(n:int, c:int):
    # Set a random seed for reproducibility (optional)
    np.random.seed(42)

    # Generate a DataFrame with random integers
    df_int = pd.DataFrame(np.random.randint(0, 100, size=(n, c)))
    print("DataFrame with random integers:")
    print(df_int)

    # Generate a DataFrame with random floats (from a standard normal distribution)
    df_float = pd.DataFrame(np.random.randn(n, c))
    print("\nDataFrame with random floats (normal distribution):")
    print(df_float)


def main():
    rand_dat_gen(10,9)
    
if __name__ == "__main__":
    main()