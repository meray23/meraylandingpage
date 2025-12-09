from openpyxl import Workbook

# Updated Data (with Company Profile + Task Management added)
data = [
    ["#", "UI Page / Item", "Duration (days)", "Start Date", "End Date"],

    [0, "Base / Structure", 10, "09/12/2025", "18/12/2025"],
    [1, "Company Profile", 2, "19/12/2025", "20/12/2025"],
    [2, "SalesPath - Leads Management", 2, "21/12/2025", "22/12/2025"],
    [3, "SalesPath - Task Management", 4, "23/12/2025", "26/12/2025"],
    [4, "Operations - Customers", 2, "27/12/2025", "28/12/2025"],
    [5, "Operations - Invoicing", 2, "29/12/2025", "30/12/2025"],
    [6, "Operations - Expenses - Vendors", 2, "31/12/2025", "01/01/2026"],
    [7, "Operations - Expenses - Expense Input", 3, "02/01/2026", "04/01/2026"],
    [8, "Operations - Expenses - Expense Invoice", 3, "05/01/2026", "07/01/2026"],
    [9, "Operations - Accounting - Chart of Accounts", 3, "08/01/2026", "10/01/2026"],
    [10, "Operations - Accounting - Manual Journals", 3, "11/01/2026", "13/01/2026"],
    [11, "Operations - Inventory", 3, "14/01/2026", "16/01/2026"],
    [12, "Operations - Payroll WPS", 6, "17/01/2026", "22/01/2026"],
    [13, "Reports", 6, "23/01/2026", "28/01/2026"],
    [14, "Business Dashboard", 3, "29/01/2026", "31/01/2026"],
    [15, "Sign up / Sign in", 3, "29/01/2026", "31/01/2026"],

    # Backend + Integration items you already listed
    [16, "Back End - Overall", 58, "05/12/2025", "01/02/2026"],
    [17, "Invoice backend - AI", 76, "15/12/2025", "28/02/2026"],
    [18, "Integration / Database - Overall", 63, "15/12/2025", "15/02/2026"],
    [19, "Testing", 30, "30/01/2026", "28/02/2026"],
    [20, "Integration & Testing (catch-up / final)", 28, "01/02/2026", "28/02/2026"],
]

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = "Schedule"

# Insert data into Excel
for row in data:
    ws.append(row)

# Save file
wb.save("schedule.xlsx")

print("Excel file 'schedule.xlsx' created successfully!")
