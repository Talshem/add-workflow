import random
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def monte_carlo_pi(num_samples: int) -> float:
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

def main():
    num_samples = 1000000
    print(f"Monte Carlo estimate of Pi with {num_samples} samples: {monte_carlo_pi(num_samples)}")
    x_vals = [random.random() for _ in range(num_samples)]
    y_vals = [random.random() for _ in range(num_samples)]
    plt.scatter(x_vals, y_vals, color='blue', s=1)
    plt.title("Monte Carlo Estimation of Pi")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()