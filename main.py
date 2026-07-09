import pandas as pd


#========================================================================================
# CALCULATE GC CONTENT
def gc_content(sequence):
    g = sequence.count("G")
    c = sequence.count("C")

    gc = ((g + c) / len(sequence)) * 100
    return round(gc , 2)


# CLASSIFY GENES BASED ON SEQUENCE LENGTH
def category(length):
    if length < 18:
        return "Short"
    elif length <= 2:
        return "Medium"
    else:
        return "Long"


# ALL GENES
def show_all_genes(data):
    print()
    print("All Genes:")
    print(data)


# SUMMURY
def show_summury(data):
    print()
    print("Summury Statistics:")
    print(data.describe())


# FOUND THE GENE USER WANTS
def search_gene(data):

    gene_name = input("Enter gene name: ")
    gene = data[data["Gene"] == gene_name]

    if gene.empty:
        print("Gene not found")
    else:
        result = gene.iloc[0]

        print("Gene found!")
        print()

        for column in result.index:
            print(f"{column}: {result[column]}")


# TOP 3 LONGEST GENES
def show_top3(data):

    print()
    print("Top 3 longest genes: ")

    top3 = data.sort_values(by = "Length" , ascending = False).head(3)
    print(top3[["Gene" , "DNA" , "Length"]])


# LONGEST GENE
def show_longest_gene(data):

    print()
    print("Longest gene: ")

    longest_gene = data.sort_values(by = "Length" , ascending = False).iloc[0]

    for column in longest_gene.index:
        print(f"{column}: {longest_gene[column]}")



# FILTERED GC CONTENT
def gc_filtered(data):

    print()
    minimum_gc = float(input("Enter minimun gc content:"))
    filtered_gc = data[data["GC_Content"] >= minimum_gc]

    if filtered_gc.empty:
        print("No genes found.")
    else:
        print(filtered_gc[["Gene" , "Length" , "GC_Content"]])  



#================================================================================================
# READ INPUT CSV FILE
data = pd.read_csv("genes.csv")


# CREATE NEW ANALYSIS COLUMNS + DISPLAY RESULTS
data["Length"] = data["DNA"].str.len()
data["GC_Content"] = data["DNA"].apply(gc_content)
data["Category"] = data["Length"].apply(category)


# EXPORT RESULTS TO A NEW CSV FILE
data.to_csv("analysis_results.csv" , index = False)
print("Results saved to analysis_results.csv")



#================================================================================================
# MENU
while True:

    print("\n===== DNA Statistics Analyzer =====")
    print("1. Show all genes")
    print("2. Show summary")
    print("3. Search gene")
    print("4. Top 3 longest genes")
    print("5. Filter by GC content")
    print("6. Show longest gene")
    print("7. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        show_all_genes(data)
    elif choice == "2":
        show_summury(data)
    elif choice == "3":
        search_gene(data)
    elif choice == "4":
        show_top3(data)
    elif choice == "5":
        gc_filtered(data)
    elif choice == "6":
        show_longest_gene(data)
    elif choice == "7":
        print("Exit")
        break
    else:
        print("Invalid choice!")    
