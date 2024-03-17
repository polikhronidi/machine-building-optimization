# Optimization Toolkit

Optimization Toolkit is a Python script designed to facilitate multi-objective optimization in engineering applications. It offers a flexible framework to optimize systems while considering technical, economic, and environmental factors. By leveraging the SciPy library, this toolkit provides efficient optimization algorithms, ensuring robust solutions that meet diverse requirements.

## Key Features

- **Multi-objective Optimization:** Incorporate multiple objectives, such as technical performance, cost, and environmental impact, into the optimization process.

- **Constraint Handling:** Define constraints on variables to ensure feasibility in real-world engineering problems.

- **Customizable Weights:** Assign weights to each objective to reflect their relative importance in the optimization process.

- **Interactive Interface:** User-friendly text-based interface guides users through inputting weights, initial variable values, and displays optimization results.

## Usage

1. **Installation:** Ensure you have Python 3.x installed along with the required dependencies listed in `requirements.txt`. You can install the dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

2. **Running the Script:** Run the `optimization.py` script:

    ```bash
    python optimization.py
    ```

3. **Input Parameters:** Follow the prompts to provide weights for each category (technical, economic, environmental) and initial variable values.

4. **Optimization Results:** The script will perform optimization and display the optimal variable values along with the minimum function value.

## Example
Here's a simple example demonstrating how to use the Optimization Toolkit:

```bash
$ python optimization.py
```
Enter weights for each category (technical, economic, environmental):
Technical: 0.4
Economic: 0.3
Environmental: 0.3
Enter initial variable values:
Variable 1: 2
Variable 2: 3

Optimal variable values: [1.5 8. ]
Minimum function value: 25.0
