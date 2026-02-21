import numpy as np
import pandas as pd

def run_topsis(input_file, output_file):
    data = pd.read_csv(input_file)

    matrix = data.iloc[:, 1:].values
    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    weights = np.ones(norm.shape[1])
    weighted = norm * weights

    ideal_best = np.max(weighted, axis=0)
    ideal_worst = np.min(weighted, axis=0)

    d_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    scores = d_neg / (d_pos + d_neg)

    data["Topsis Score"] = scores
    data["Rank"] = data["Topsis Score"].rank(ascending=False)

    data.to_csv(output_file, index=False)
    print(f"\nTOPSIS Result: {output_file}")
    print(data)


run_topsis("results/politics_metrics.csv", "results/politics_topsis.csv")
run_topsis("results/sports_metrics.csv", "results/sports_topsis.csv")
run_topsis("results/medicine_metrics.csv", "results/medicine_topsis.csv")

