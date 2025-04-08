import pandas as pd

def extract_experience(text):
    jd = text.lower().replace('-', ' to ')
    words = jd.split()
    # print(words)

    for i, word in enumerate(words):
        # Case: "minimum of X years or minimum X yrs or years"
        if (word == "minimum" and i + 2 < len(words)) or (word=='minimum' and i+1<len(words)) :
            if (words[i + 1] == "of" and words[i + 2].isdigit()):
                x = int(words[i + 2])
                return f"{x} - {x + 2} years"
            elif words[i+1].isdigit():
                x=int(words[i+1])
                return f"{x} - {x+2} years"

        # Case: "maximum of X years or maximum X years or yrs"
        if (word == "maximum" and i + 2 < len(words)) or (word=='maximum' and i+1<len(words)) :
            if words[i + 1] == "of" and words[i + 2].isdigit():
                x = int(words[i + 2])
                return f"{max(0, x - 2)} - {x} years"
            elif words[i+1].isdigit():
                x=int(words[i+1])
                return f"{max(0, x - 2)} - {x} years"

        # Case: "at least X years"
        if word == "least" and i > 0 and (words[i - 1] == "at" or words[i-1]=="At") and i + 1 < len(words) and words[i + 1].isdigit():
            x = int(words[i + 1])
            return f"{x} - {x + 2} years"

        # Case: "X to Y years"
        if word == "to" and i > 0 and i < len(words) - 1:
            if words[i - 1].isdigit() and words[i + 1].isdigit():
                return f"{words[i - 1]} - {words[i + 1]} years"

        # Case: "X+ years" or "X years"
        if (word.endswith("years") or word.endswith("yrs") or word.endswith("year's")) and i > 0:
            val = words[i - 1].replace("+", "")
            if val.isdigit():
                x = int(val)
                return f"{x} - {x + 2} years"

    return "Experience not mentioned"

# Test cases
test = [
    "We are looking for a software developer with 3+ yrs of experience in Python.",
    "Minimum of 5 years experience in data analytics is required.",
    "Minimum 5 years experience in data analytics is required.",
    "Minimum 6 yrs experience in data analytics is required.",
    "Maximum of 6 years experience in frontend development.",
    "1+ years of experience in Python development; knowledge of Pyspark, Django, and SQL",
    "Candidates should have at least 5 yrs of relevant experience.",
    "At least 8 years of experience in software development",
    "5+ years of professional/industrial experience in software development.",
    "5+ year's of professional/industrial experience in software development.",
    "3+ yrs industry hands-on professional experience in Frontend software development.",
    "2 to 4 years of technical experience with WebSphere Transformation Extender (WTX)",
    "Experience 2-4 years",
    "Have expertise in Object-oriented design principles using any modern language preferably Java.Bachelor of Technology / Engineering in Computer Science or a related technical discipline with 2 to 4 years of relevant experience",
    "Minimum 1+ years of experience in Golang development.",
    "2+ years of professional non-internship marketing experience",
    "1+ years of experience in Python development; knowledge of Pyspark, Django, and SQL",
    "Experience: Between 3 - 5 years of software development experience",
    " Angular & Bootstrap: Experience with Angular 12+ yrs and Bootstrap, as well as a strong grasp of the modern JavaScript development tool chain.",
]

# Run tests
results=[]
for jd in test:
    result = extract_experience(jd)
    results.append({"JD Phrase Example":jd, "Normalized Range":result})
    # print(f"JD: {jd}\nNormalized Experience: {result}\n")

df = pd.DataFrame(results)

output_file = "job_experience.xlsx"
df.to_excel(output_file, index=False)

print(f"Results saved to '{output_file}' successfully.")
