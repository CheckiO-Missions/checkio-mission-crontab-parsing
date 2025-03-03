"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["* * * * *", "2025-03-03T14:30"],
            "answer": "2025-03-03T14:31",
            "explanation": "Simple every minute"
        },
        {
            "input": ["*/15 * * * *", "2025-03-03T14:30"],
            "answer": "2025-03-03T14:45",
            "explanation": "Every 15 minutes"
        },
        {
            "input": ["5,10,15,20 * * * *", "2025-03-03T14:07"],
            "answer": "2025-03-03T14:10",
            "explanation": "Specific minutes"
        },
        {
            "input": ["10-20 * * * *", "2025-03-03T14:05"],
            "answer": "2025-03-03T14:10",
            "explanation": "Range of minutes"
        },
        {
            "input": ["10-30/5 * * * *", "2025-03-03T14:12"],
            "answer": "2025-03-03T14:15",
            "explanation": "Range with step"
        },
        {
            "input": ["@daily", "2025-03-03T14:30"],
            "answer": "2025-03-04T00:00",
            "explanation": "Special keyword @daily"
        },
    ],
    "Extra": [
        {
            "input": ["0 5 * * *", "2025-03-03T14:30"],
            "answer": "2025-03-04T05:00",
            "explanation": "Specific hour"
        },
        {
            "input": ["30 * * * *", "2025-03-03T14:15"],
            "answer": "2025-03-03T14:30",
            "explanation": "Every hour at 30 minutes"
        },
        {
            "input": ["0 8-17 * * *", "2025-03-03T18:30"],
            "answer": "2025-03-04T08:00",
            "explanation": "Range of hours"
        },
        {
            "input": ["0 8-17/3 * * *", "2025-03-03T10:30"],
            "answer": "2025-03-03T11:00",
            "explanation": "Range of hours with step"
        },
        {
            "input": ["0 0 * * *", "2025-03-03T14:30"],
            "answer": "2025-03-04T00:00",
            "explanation": "Daily at midnight"
        },
        {
            "input": ["0 0 * * 1", "2025-03-03T14:30"],
            "answer": "2025-03-10T00:00",
            "explanation": "Every Monday at midnight"
        },
        {
            "input": ["0 12 * * 0,6", "2025-03-03T14:30"],
            "answer": "2025-03-08T12:00",
            "explanation": "Every weekend (Saturday and Sunday)"
        },
        {
            "input": ["0 0 1 * *", "2025-03-03T14:30"],
            "answer": "2025-04-01T00:00",
            "explanation": "First day of every month"
        },
        {
            "input": ["0 0 29 2 *", "2024-01-15T10:00"],
            "answer": "2024-02-29T00:00",
            "explanation": "Last day of February (leap year 2024)"
        },
        {
            "input": ["0 0 29 2 *", "2025-01-15T10:00"],
            "answer": "2028-02-29T00:00",
            "explanation": "Last day of February (non-leap year 2025)"
        },
        {
            "input": ["0 0 1 * 1", "2025-03-03T14:30"],
            "answer": "2025-09-01T00:00",
            "explanation": "Using day of month AND day of week"
        },
        {
            "input": ["@monthly", "2025-03-03T14:30"],
            "answer": "2025-04-01T00:00",
            "explanation": "Special keyword @monthly"
        },
        {
            "input": ["30 */3 * * 1-5", "2025-03-01T14:40"],
            "answer": "2025-03-03T00:30",
            "explanation": "30 minutes past every 3rd hour on weekdays"
        },
        {
            "input": ["45 12 * * *", "2025-03-03T12:45"],
            "answer": "2025-03-04T12:45",
            "explanation": "Exact minute match"
        },
    ]
}
