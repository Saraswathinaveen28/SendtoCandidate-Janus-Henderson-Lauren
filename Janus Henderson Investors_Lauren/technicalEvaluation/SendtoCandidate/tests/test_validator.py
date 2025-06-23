import pandas as pd
import os
from typing import List, Dict, Tuple
import json
from datetime import datetime

class DataValidator:
    def __init__(self, files_dir: str, requirements_file: str):
        self.files_dir = files_dir
        self.requirements_file = requirements_file
        self.requirements_df = pd.read_excel(requirements_file)
        self.test_results = []
        
    def check_duplicate_columns(self, file_path: str) -> Tuple[bool, List[str]]:
        """
        Test Scenario 1: Check for duplicate columns in a file
        Returns: (has_duplicates, list_of_duplicate_columns)
        """
        try:
            # Read the file based on its extension
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                df = pd.DataFrame(data)
            else:
                return False, []
            
            # Get list of columns
            columns = df.columns.tolist()
            # Find duplicates
            duplicates = [col for col in columns if columns.count(col) > 1]
            return len(duplicates) > 0, duplicates
            
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return False, []
    
    def validate_yes_no_fields(self, file_path: str) -> Tuple[bool, List[str]]:
        """
        Test Scenario 2: Validate Yes/No type fields
        Returns: (is_valid, list_of_invalid_fields)
        """
        try:
            # Read the file based on its extension
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                df = pd.DataFrame(data)
            else:
                return True, []
            
            invalid_fields = []
            
            # Get Yes/No fields from requirements
            yes_no_fields = self.requirements_df[
                self.requirements_df['Response Type'].str.contains('Yes/No', case=False, na=False)
            ]['Attribute Field Name'].tolist()
            
            # Check each Yes/No field in the file
            for field in yes_no_fields:
                if field in df.columns:
                    # Check if all values are either 'Yes' or 'No'
                    invalid_values = df[field].dropna().apply(
                        lambda x: str(x).strip().lower() not in ['yes', 'no']
                    )
                    if invalid_values.any():
                        invalid_fields.append(field)
            
            return len(invalid_fields) == 0, invalid_fields
            
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            return False, []

def generate_html_report(test_results: List[Dict], output_path: str):
    """
    Generate an HTML report from test results
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Validation Test Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .container {{ max-width: 1200px; margin: 0 auto; }}
            .header {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
            .test-section {{ margin: 20px 0; }}
            .test-case {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }}
            .pass {{ color: green; }}
            .fail {{ color: red; }}
            .timestamp {{ color: #666; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Data Validation Test Report</h1>
                <p class="timestamp">Generated on: {timestamp}</p>
            </div>
    """.format(timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Add test results
    for result in test_results:
        html_content += f"""
            <div class="test-section">
                <h2>{result['test_name']}</h2>
                <div class="test-case">
                    <p><strong>File:</strong> {result['file']}</p>
                    <p><strong>Status:</strong> <span class="{result['status'].lower()}">{result['status']}</span></p>
                    {f"<p><strong>Details:</strong> {result['details']}</p>" if result['details'] else ""}
                </div>
            </div>
        """

    html_content += """
        </div>
    </body>
    </html>
    """

    # Ensure the evidence directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the HTML report
    with open(output_path, 'w') as f:
        f.write(html_content)

def run_tests():
    # Initialize validator
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files_dir = os.path.join(base_dir, 'files')
    requirements_file = os.path.join(base_dir, 'requirements', 'Data Fields_New.xlsx')
    evidence_dir = os.path.join(base_dir, 'evidence')
    
    validator = DataValidator(files_dir, requirements_file)
    
    # Get all y_*.csv files
    test_files = [f for f in os.listdir(files_dir) if f.startswith('y_') and f.endswith('.csv')]
    
    print("\n=== Test Results ===")
    
    # Test Scenario 1: Check for duplicate columns
    print("\nTest Scenario 1 - Checking for duplicate columns:")
    for file in test_files:
        file_path = os.path.join(files_dir, file)
        has_duplicates, duplicates = validator.check_duplicate_columns(file_path)
        status = "FAIL" if has_duplicates else "PASS"
        print(f"\n{file}: {status}")
        if has_duplicates:
            print(f"Duplicate columns found: {duplicates}")
        
        validator.test_results.append({
            'test_name': 'Duplicate Columns Check',
            'file': file,
            'status': status,
            'details': f"Duplicate columns found: {duplicates}" if has_duplicates else "No duplicate columns found"
        })
    
    # Test Scenario 2: Validate Yes/No fields
    print("\nTest Scenario 2 - Validating Yes/No fields:")
    for file in test_files:
        file_path = os.path.join(files_dir, file)
        is_valid, invalid_fields = validator.validate_yes_no_fields(file_path)
        status = "FAIL" if not is_valid else "PASS"
        print(f"\n{file}: {status}")
        if not is_valid:
            print(f"Invalid Yes/No fields found: {invalid_fields}")
        
        validator.test_results.append({
            'test_name': 'Yes/No Fields Validation',
            'file': file,
            'status': status,
            'details': f"Invalid Yes/No fields found: {invalid_fields}" if not is_valid else "All Yes/No fields are valid"
        })
    
    # Generate HTML report
    report_path = os.path.join(evidence_dir, 'validation_report.html')
    generate_html_report(validator.test_results, report_path)
    print(f"\nHTML report generated at: {report_path}")

if __name__ == "__main__":
    run_tests() 