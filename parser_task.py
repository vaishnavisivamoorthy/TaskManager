import dateparser
from datetime import datetime
import re

def parse_task(text):
    priority = "Normal"
    text_lower = text.lower()

    # Priority detection
    if "high priority" in text_lower:
        priority = "High"
    elif "low priority" in text_lower:
        priority = "Low"

    # Date parsing with multiple patterns
    date_patterns = [
        r"(?:on|at|by|before|after|next|on the|due)\s+(.+?)(?:\s+high priority|\s+low priority|$)",
        r"tomorrow(?: at)?\s*(\d{1,2}(?:am|pm)?)?",
        r"next\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
        r"\d{1,2}(?:st|nd|rd|th)?\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*(?:\d{4})?"
    ]

    date_str = None
    for pattern in date_patterns:
        match = re.search(pattern, text_lower, re.IGNORECASE)
        if match:
            date_str = match.group(1) if match.groups() else match.group(0)
            break

    due_date = None
    if date_str:
        dt = dateparser.parse(
            date_str,
            settings={
                'PREFER_DATES_FROM': 'future',
                'RELATIVE_BASE': datetime.now(),
                'RETURN_AS_TIMEZONE_AWARE': False,
                'DATE_ORDER': 'DMY'
            }
        )
        if dt:
            due_date = dt.strftime("%Y-%m-%d %H:%M:%S")

    # Title extraction
    title = re.sub(
        r'(?:high priority|low priority|on|at|by|before|after|next|tomorrow|\d{1,2}(?:st|nd|rd|th)?\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*).*$',
        '', 
        text, 
        flags=re.IGNORECASE
    ).strip()

    return title, due_date, priority