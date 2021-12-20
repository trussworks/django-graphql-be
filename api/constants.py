"""Constant values for the API"""

# Color coding for SITH cases; denotes severity
COLOR_CODE_GRAY = "gray"
COLOR_CODE_BLUE = "blue"
COLOR_CODE_PURPLE = "purple"
COLOR_CODE_BROWN = "brown"

COLOR_CODE_CHOICES = [
    # (database value, display value)
    (COLOR_CODE_GRAY, COLOR_CODE_GRAY),
    (COLOR_CODE_BLUE, COLOR_CODE_BLUE),
    (COLOR_CODE_PURPLE, COLOR_CODE_PURPLE),
    (COLOR_CODE_BROWN, COLOR_CODE_BROWN),
]

# Status options for SITH cases
STATUS_PRE_INQUIRY = "pre-inquiry"
STATUS_IN_PROGRESS = "in progress"
STATUS_INACTIVE = "zero - inactive"

STATUS_CHOICES = [
    # (database value, display value)
    (STATUS_PRE_INQUIRY, STATUS_PRE_INQUIRY),
    (STATUS_IN_PROGRESS, STATUS_IN_PROGRESS),
    (STATUS_INACTIVE, STATUS_INACTIVE),
]
