Usage Page (Desktop),               ; Generic desktop controls (01h)
Usage (Keyboard),                   ; Keyboard (06h, application collection)
Collection (Application),
    Usage Page (Keyboard),          ; Keyboard/keypad (07h)
    Usage Minimum (KB Leftcontrol), ; Keyboard left control (E0h, dynamic value)
    Usage Maximum (KB Right GUI),   ; Keyboard right GUI (E7h, dynamic value)
    Logical Minimum (0),
    Logical Maximum (1),
    Report Size (1),
    Report Count (8),
    Input (Variable),
    Report Count (1),
    Report Size (8),
    Input (Constant),
    Report Count (5),
    Report Size (1),
    Usage Page (LED),               ; LEDs (08h)
    Usage Minimum (01h),
    Usage Maximum (05h),
    Output (Variable),
    Report Count (1),
    Report Size (3),
    Output (Constant),
    Report Count (6),
    Report Size (8),
    Logical Minimum (0),
    Logical Maximum (255),
    Usage Page (Keyboard),          ; Keyboard/keypad (07h)
    Usage Minimum (None),           ; No event (00h, selector)
    Usage Maximum (FFh),
    Input,
End Collection
