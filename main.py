import htmlprep as prep

htmlfile = prep.htmlgen("temp")


with open("input.txt", "r") as f:
    text = f.read()
    text = "".join(text)
htmlfile.text_processor(text)
