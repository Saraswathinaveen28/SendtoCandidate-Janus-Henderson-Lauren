# Data Validation Proof of Concept

## Overview

Thank you for sharing the technical test. I’ve completed it and included all necessary components, along with test evidence to support the solution. To enhance understanding, I’ve also added the following supporting documentation:

- **data_file_requirements.pdf** – outlining the data requirements
- **explanation_to_stakeholders.pdf** – a simplified overview for non-technical stakeholders
- **test_report.md** and **validation_report.html** – included under the `technical_evaluation` folder as test evidence
- **test_validator.py** – the main test file, located in the `tests` folder

## Pre-requisite

Please ensure Python is installed on your system to run the test.

## Objectives

- **Automate validation** of report files to ensure consistency with regulatory requirements.
- **Implement two key test scenarios**:
  1. **Duplicate Column Check**: Ensure no column is reported more than once in any file.
  2. **[Yes/No] Field Validation**: Ensure all fields defined as [Yes/No] in the requirements contain only valid responses.
- **Provide clear, actionable reports** for both technical and non-technical stakeholders.
- **Enable maintainability and scalability** for future enhancements and additional validation rules.

## Repository Structure

```
SendtoCandidate/
│
├── evidence/
│   ├── test_report.md                # Markdown summary of test results and findings
│   └── validation_report.html        # Detailed HTML report of test execution
│
├── technical_evaluation/
│   ├── test_report.md                # Test evidence (duplicate for clarity)
│   └── validation_report.html        # Test evidence (duplicate for clarity)
│
├── files/
│   ├── y_*.csv                       # Report files under test (scope limited to these files)
│   ├── parameters.csv
│   └── report.json
│
├── requirements/
│   ├── Data Fields_New.xlsx          # Excel file containing data field definitions and requirements
│   └── data_file_requirements.pdf    # PDF outlining the data requirements
│
├── documentation/
│   └── explanation_to_stakeholders.pdf # Overview for non-technical stakeholders
│
├── tests/
│   └── test_validator.py             # Main test script implementing validation logic
│
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation (this file)
```

## Step-by-Step Guide

Follow these steps to set up, run, and review the results of the data validation Proof of Concept:

### 1. Clone the Repository

## Clone the project to your local machine:

```sh
git clone https://github.com/Saraswathinaveen28/SendtoCandidate-Janus-Henderson-Lauren.git
cd SendtoCandidate-Janus-Henderson-Lauren

```

### 2. Install Python and Dependencies

Ensure Python 3.8 or higher is installed. Then, install all required packages:
```sh
pip install -r requirements.txt
```

### 3. Review Supporting Documentation

- **data_file_requirements.pdf:** Understand the data requirements and validation criteria.
- **explanation_to_stakeholders.pdf:** Get a high-level overview tailored for non-technical stakeholders.

### 4. Prepare Input Files

- Place your report files (matching `y_*.csv`) in the `files/` directory.
- Ensure the requirements file (`Data Fields_New.xlsx`) is present in the `requirements/` folder.

### 5. Run the Validation Script

Navigate to the `tests` directory and execute the main test script:
```sh
cd tests
python test_validator.py
```

### 6. Review Test Evidence

After execution, review the generated reports:
- **evidence/validation_report.html:** Detailed, user-friendly HTML report.
- **evidence/test_report.md:** Concise Markdown summary of findings.

Alternatively, check the same reports under the `technical_evaluation` folder.

### 7. Interpret Results

- Review the reports for any failed validations or issues.
- Use the documentation to understand the context and next steps.

### 8. Next Steps

- Address any issues highlighted in the reports.
- For further enhancements or contributions, refer to the [Potential Additions](#potential-additions) section.

---

## Test Scenarios

### 1. Duplicate Column Check

- **Purpose**: Ensures that no column appears more than once in any report file.
- **Scope**: All files matching `y_*.csv` in the `files/` directory.
- **Outcome**: PASS if all columns are unique per file; FAIL if duplicates are found.

### 2. [Yes/No] Field Validation

- **Purpose**: Validates that all fields defined as [Yes/No] in the requirements contain only "Yes" or "No" (case-insensitive).
- **Scope**: All files matching `y_*.csv` in the `files/` directory, cross-referenced with `requirements/Data Fields_New.xlsx`.
- **Outcome**: PASS if all values are valid; FAIL if any invalid values are detected.

## Reporting

- **HTML Report**: A user-friendly, detailed report is generated at `evidence/validation_report.html`.
- **Markdown Summary**: A concise summary with findings and recommendations is available at `evidence/test_report.md`.

## Key Assumptions

- Only files matching `y_*.csv` are in scope for validation.
- The requirements Excel file is the single source of truth for field definitions.
- [Yes/No] fields are case-insensitive; empty or null values are considered invalid.
- The solution is designed to be easily maintainable as requirements evolve.

## Potential Issues and Recommendations

- **Data Type Inconsistencies**: Variations such as "YES", "NO", "Y", "N" may exist. Standardization is recommended.
- **Requirements Management**: Version control and change management for the requirements file are advised.

## Extensibility

- The framework is designed for easy extension to additional validation rules.
- Future enhancements may include more detailed error reporting, a user interface, automated scheduling, and integration with version control for requirements.

## Potential Additions

To further enhance the project’s usability, maintainability, and transparency, consider the following additions:

- **License:**  
  Add a LICENSE file to clarify usage rights and distribution terms for this project.

- **Contributing Guidelines:**  
  Include a `CONTRIBUTING.md` file with instructions for those who wish to contribute, outlining coding standards, pull request processes, and communication channels.

- **Sample Data:**  
  Provide a sample `y_*.csv` file in the `files/` directory to help users quickly understand the expected input format and facilitate testing.

- **Error Handling Documentation:**  
  Briefly describe how the solution handles errors or failed validations, and where users can find logs or error messages.

- **Dependencies:**  
  Ensure all required Python packages are listed in `requirements.txt`, and specify any system-level dependencies if applicable.

- **Version Information:**  
  Add versioning details for the PoC and major dependencies to help with reproducibility and maintenance.

- **Known Limitations:**  
  Document any known limitations or edge cases that are not currently addressed by the solution.

---

## Contact

For questions or further information, please contact the project owner or regulatory team lead.

---

*This PoC demonstrates a maintainable, scalable, and user-friendly approach to automated data validation for
