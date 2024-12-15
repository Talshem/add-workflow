import numpy as np

def monte_carlo_pi(num_samples: int) -> float:
    x = np.random.random(num_samples)
    y = np.random.random(num_samples)
    inside_circle = np.sum(x**2 + y**2 <= 1)
    return (inside_circle / num_samples) * 4

def main():
    num_samples = 1000000
    print(f"Monte Carlo estimate of Pi with {num_samples} samples: {monte_carlo_pi(num_samples)}")

if __name__ == "__main__":
    main()