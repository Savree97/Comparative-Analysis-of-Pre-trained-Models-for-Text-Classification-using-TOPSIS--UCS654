from datasets import load_dataset

# Load AG News dataset (Text Classification)
dataset = load_dataset("ag_news")

print(dataset)

medical_dataset = load_dataset("pubmed_qa", "pqa_labeled")
print(medical_dataset)
