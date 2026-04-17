# 🧬 DNA Complement Generator (Python | If/Else Logic | VS Code)

## 📌 Overview

The DNA Complement Generator is a Python-based application designed to generate the complementary strand of a given DNA sequence.

This project applies fundamental programming concepts—specifically conditional (`if / else`) statements—to transform biological sequence data. It is implemented and executed within the Visual Studio Code (VS Code) environment, providing a structured workflow for development and testing.

---

## 🎯 Objectives

* Generate complementary DNA sequences using `if / else` logic
* Apply basic programming principles to biological data processing
* Develop and execute Python programs using Visual Studio Code
* Strengthen understanding of nucleotide pairing rules

---

## 🧬 Biological Background

DNA consists of four nucleotide bases:

* Adenine (**A**)
* Thymine (**T**)
* Cytosine (**C**)
* Guanine (**G**)

Base pairing rules:

* A pairs with T
* T pairs with A
* C pairs with G
* G pairs with C

The complementary strand of a DNA sequence is formed by replacing each base with its pair.

---

## ⚙️ Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code
* **Concepts:** Conditional statements (`if`, `elif`, `else`)

---

## 📂 Project Structure

```text
dna-complement-generator/
│
├── complement.py
└── README.md
```

---

## 🖥️ Development Environment (VS Code)

This project was developed using Visual Studio Code with:

* Python extension installed
* Integrated terminal for execution
* Basic debugging and file management tools

---

## ▶️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dna-complement-generator.git
```

### 2. Open in VS Code

* Launch Visual Studio Code
* Select **File → Open Folder**
* Choose the project directory

### 3. Verify Python Installation

In the VS Code terminal:

```bash
python --version
```

---

## 🚀 Usage (VS Code)

### Step 1:

Open `complement.py` in VS Code

### Step 2:

Run the program:

* Click ▶️ “Run Python File”
  **OR**
* Use terminal:

```bash
python complement.py
```

### Step 3:

Enter a DNA sequence when prompted

---

## 📊 Example

### Input

```text
ATCG
```

### Output

```text
TAGC
```

---

## 🧠 Methodology

1. Accept DNA sequence input from the user
2. Convert input to uppercase for consistency
3. Initialize an empty string for the complement
4. Iterate through each base in the sequence
5. Use `if / elif / else` statements to:

   * Replace each base with its complementary pair
6. Return the generated complementary sequence

---

## 🧪 Core Logic (If/Else Implementation)

```python
sequence = input("Enter DNA sequence: ").upper()
complement = ""

for base in sequence:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "C":
        complement += "G"
    elif base == "G":
        complement += "C"
    else:
        complement += "?"  # handles invalid input

print("Complementary DNA sequence:", complement)
```

---

## 🔬 Applications

* Introductory bioinformatics analysis
* DNA sequence transformation tasks
* Educational tool for understanding base pairing

---

## 🚧 Limitations

* Does not validate input sequence strictly
* Handles invalid characters with placeholder output
* Not optimized for large datasets

---

## 🔮 Future Improvements

* Add strict validation for DNA sequences
* Support file input (e.g., `.txt`, `.fasta`)
* Generate reverse complement sequences
* Improve error handling and reporting

---

## 👨‍🔬 Author

Godwin Samuel |BSc Biochemistry | Aspiring Bioinformatician

---

## 📄 License

This project is licensed under the MIT License.
