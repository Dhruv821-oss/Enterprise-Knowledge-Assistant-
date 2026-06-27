TEST_DATA = [

    # =====================================================
    # HR Policy
    # =====================================================

    {
        "question": "How many paid leaves does an employee receive?",
        "expected_answer": "Employees receive 24 paid leaves every calendar year.",
        "expected_sources": ["HR_Policy.pdf"]
    },

    {
        "question": "How many sick leaves are provided?",
        "expected_answer": "Employees receive 10 paid sick leaves annually.",
        "expected_sources": ["HR_Policy.pdf"]
    },

    {
        "question": "What is the probation period?",
        "expected_answer": "The probation period is 6 months.",
        "expected_sources": ["HR_Policy.pdf"]
    },

    {
        "question": "What are the standard working hours?",
        "expected_answer": "Working hours are 9:00 AM to 6:00 PM, Monday through Friday.",
        "expected_sources": ["HR_Policy.pdf"]
    },

    # =====================================================
    # Employee Handbook
    # =====================================================

    {
        "question": "Can employees work remotely?",
        "expected_answer": "Employees may work remotely up to two days per week with manager approval.",
        "expected_sources": ["Employee_Handbook.pdf"]
    },

    {
        "question": "What dress code should employees follow?",
        "expected_answer": "Employees should wear business casual attire in the office.",
        "expected_sources": ["Employee_Handbook.pdf"]
    },

    {
        "question": "What is expected regarding employee conduct?",
        "expected_answer": "Employees are expected to maintain professionalism and respect in the workplace.",
        "expected_sources": ["Employee_Handbook.pdf"]
    },

    # =====================================================
    # IT Security
    # =====================================================

    {
        "question": "How long should passwords be?",
        "expected_answer": "Passwords must contain at least 12 characters.",
        "expected_sources": ["IT_Security_Policy.pdf"]
    },

    {
        "question": "Is multi-factor authentication required?",
        "expected_answer": "Yes. Multi-factor authentication is mandatory for all employees.",
        "expected_sources": ["IT_Security_Policy.pdf"]
    },

    {
        "question": "What security is required for company laptops?",
        "expected_answer": "Company laptops must use full disk encryption.",
        "expected_sources": ["IT_Security_Policy.pdf"]
    },

    # =====================================================
    # Travel Policy
    # =====================================================

    {
        "question": "Who approves business travel?",
        "expected_answer": "Business travel must be approved by the employee's manager before booking.",
        "expected_sources": ["Travel_and_Expense_Policy.pdf"]
    },

    {
        "question": "What is the hotel reimbursement limit?",
        "expected_answer": "Hotel reimbursement is limited to $150 per night unless pre-approved.",
        "expected_sources": ["Travel_and_Expense_Policy.pdf"]
    },

    {
        "question": "What meal allowance is provided during travel?",
        "expected_answer": "Employees may claim up to $50 per day for meals.",
        "expected_sources": ["Travel_and_Expense_Policy.pdf"]
    },

    # =====================================================
    # Multi-document Reasoning
    # =====================================================

    {
        "question": "Summarize the leave policy and remote work policy.",
        "expected_answer": (
            "Employees receive 24 paid leaves and 10 sick leaves annually. "
            "Employees may work remotely up to two days per week with manager approval."
        ),
        "expected_sources": [
            "HR_Policy.pdf",
            "Employee_Handbook.pdf"
        ]
    },

    {
        "question": "Summarize employee benefits mentioned across all documents.",
        "expected_answer": (
            "Employees receive paid leave, sick leave, remote work options, "
            "business travel reimbursement, hotel reimbursement, and meal allowances."
        ),
        "expected_sources": [
            "HR_Policy.pdf",
            "Employee_Handbook.pdf",
            "Travel_and_Expense_Policy.pdf"
        ]
    },

    {
        "question": "What company security policies should every employee follow?",
        "expected_answer": (
            "Employees must use passwords of at least 12 characters, "
            "enable multi-factor authentication, and use encrypted company laptops."
        ),
        "expected_sources": [
            "IT_Security_Policy.pdf"
        ]
    }

]