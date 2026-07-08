import pandas as pd

#================================================
# CALCULATE GC CONTENT
#================================================
def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")

    gc = ((g + c) / len(sequence)) * 100
    return round(gc , 2)

#================================================
# CLASSIFY GENES BASED ON SEQUENCE LENGTH
#================================================
def category(length):
    if length < 18:
        return "Short"
    elif length <= 20:
        return "Medium"
    else:
        return "Long"

#================================================
# READ INPUT CSV FILE
#================================================
data = pd.read_csv("genes.csv")

#================================================
# CREATE NEW ANALYSIS COLUMNS + DISPLAY RESULTS
#================================================
data["Length"] = data["DNA"].str.len()
data["GC_Content"] = data["DNA"].apply(gc_content)
data["Category"] = data["Length"].apply(category)

print("DNA Statistics Analyser")
print()
print(data)

print()
print("Summury Statistics:")
print(data.describe())

#================================================
# EXPORT RESULTS TO A NEW CSV FILE
#================================================
data.to_csv("analysis_results.csv" , index = False)

print()
print("Results saved to analysis_results.csv")