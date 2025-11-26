import pandas as pd

# Sheet 1: Audit Overview
overview_data = {
    "Field": [
        "Audit Title", "App Name", "Auditor", "Date",
        "Platform Tested", "App Version", "Device", "Language Tested"
    ],
    "Details": [
        "UX Audit – Registration & Login", "eZhire", "[Your Name]", "[Insert Date]",
        "Android", "[Insert Version]", "[Insert Device]", "English"
    ]
}
overview_df = pd.DataFrame(overview_data)

# Sheet 2: Test Steps
test_steps_data = {
    "Step No.": [1, 2, 3, 4, 5],
    "Action Performed": [
        "Open app", "Tap “Continue with Email”", "Enter invalid email",
        "Press back", "Switch language to Arabic"
    ],
    "Expected Result": [
        "Home screen loads", "Email input screen appears", "Should show validation error",
        "Return to welcome screen", "UI switches"
    ],
    "Actual Result": [
        "Home screen appears", "Email screen shown", "No error shown",
        "Works as expected", "Works correctly"
    ],
    "Pass/Fail": ["✅", "✅", "❌", "✅", "✅"],
    "Comments": [
        "N/A", "-", "Missing validation", "-", "Arabic button could be clearer"
    ]
}
test_steps_df = pd.DataFrame(test_steps_data)

# Sheet 3: Issues Log
issues_log_data = {
    "Issue ID": ["UX-001", "UX-002", "UX-003", "UX-004", "UX-005"],
    "Screen / Area": ["Onboarding", "Registration Icons", "Email Field", "Progress Indicator", "Country Code"],
    "Description": [
        "Tagline is unreadable due to low contrast",
        "No label for social icons",
        "Placeholder says 'Enter mail' – unprofessional",
        "1/3 indicator has no context",
        "Defaulted to Pakistan without prompt"
    ],
    "Screenshot Attached": ["Yes"] * 5,
    "Severity": ["Medium", "Medium", "Low", "Low", "Medium"],
    "Recommendation": [
        "Add overlay or increase font contrast",
        "Add “Continue with Google/Facebook” below icons",
        "Use “Enter your email”",
        "Add labels (e.g., Email > OTP > Profile)",
        "Add searchable country picker"
    ],
    "Status": ["Open"] * 5
}
issues_log_df = pd.DataFrame(issues_log_data)

# Sheet 4: Follow-Up Actions
follow_up_data = {
    "Action Item": [
        "File issues in Jira", "Review with design team", "Retest after fix"
    ],
    "Assigned To": ["UX Auditor", "UX Lead", "QA Team"],
    "Target Date": ["[Insert Date]"] * 3,
    "Status": ["⏳ In Progress", "⏳ Not Started", "🔜 Scheduled"],
    "Notes": ["-", "-", "-"]
}
follow_up_df = pd.DataFrame(follow_up_data)

# Save all sheets into an Excel file
with pd.ExcelWriter("UX_Audit_Report_eZhire.xlsx", engine="xlsxwriter") as writer:
    overview_df.to_excel(writer, sheet_name="Audit Overview", index=False)
    test_steps_df.to_excel(writer, sheet_name="Test Steps", index=False)
    issues_log_df.to_excel(writer, sheet_name="Issues Log", index=False)
    follow_up_df.to_excel(writer, sheet_name="Follow-Up Actions", index=False)

print("✅ UX Audit Excel report generated: UX_Audit_Report_eZhire.xlsx")
