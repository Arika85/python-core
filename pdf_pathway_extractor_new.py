import os
import PyPDF2

# pathways to search
pathways = [
    "Glycolysis / Gluconeogenesis",
    "Citrate cycle (TCA cycle)",
    "Pentose phosphate pathway",
    "Pentose and glucuronate interconversions",
    "Fructose and mannose metabolism",
    "Galactose metabolism",
    "Ascorbate and aldarate metabolism",
    "Fatty acid biosynthesis",
    "Fatty acid elongation",
    "Fatty acid degradation",
    "Synthesis and degradation of ketone bodies",
    "Cutin, suberine and wax biosynthesis",
    "Steroid biosynthesis",
    "Primary bile acid biosynthesis",
    "Secondary bile acid biosynthesis",
    "Ubiquinone and other terpenoid-quinone biosynt...",
    "Steroid hormone biosynthesis",
    "Oxidative phosphorylation",
    "Photosynthesis",
    "Photosynthesis - antenna proteins",
    "Arginine biosynthesis",
    "Purine metabolism",
    "Puromycin biosynthesis",
]

# cleaning the pathway list
new_pathways = []
for i in pathways:
    words = i.split(" ")
    words = [e for e in words if e not in ("/", "-", "and", "of")]
    new_pathways.append(words)
    # print(words)
# new_pathways[:10]

cleaned_pathways = []
for i in range(len(new_pathways)):
    for j in new_pathways[i]:
        cleaned_pathways.append(j)

# function
def pathwyas_extractor_new(folder_name):
    """This function takes folder name or folder path as an imput check file if it's pdf
    and then search for pathways in all the pdf files"""
    for foldername, subfolders, files in os.walk(folder_name):
        # print(folder_name)
        files = [fi for fi in files if fi.endswith(".pdf")]
        # print(files)
        for index, item in enumerate(files):  # note: don't use list
            # if item == file_name:  # if not index: # or
            # open the pdf file
            # print(item)
            reader = PyPDF2.PdfFileReader(os.path.join(foldername, item))
            # print(type(reader))

            # get number of pages
            NumPages = reader.getNumPages()
            # print(NumPages)

            # extract text and do the search
            for i in range(0, NumPages):
                PageObj = reader.getPage(i)
                print("This is page " + str(i))
                Text = PageObj.extractText().lower()
                res = [ele for ele in cleaned_pathways if (ele.lower() in Text)]
                # return res
                print(f"Pathways present: {res}")
