from happytransformer import HappyTextClassification


happy_tc = HappyTextClassification("BERT", "ProsusAI/finbert", num_labels=3)
result = happy_tc.classify_text("Tesla's stock just increased by 20%")

print(result)
print(result.label)
print(result.score)