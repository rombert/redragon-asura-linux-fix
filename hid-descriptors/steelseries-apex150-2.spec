Usage Page (Consumer),      ; Consumer (0Ch)
Usage (Consumer Control),   ; Consumer control (01h, application collection)
Collection (Application),
    Report ID (1),
    Usage Page (Consumer),  ; Consumer (0Ch)
    Usage Minimum (00h),
    Usage Maximum (0FFFh),
    Logical Minimum (0),
    Logical Maximum (4095),
    Report Size (16),
    Report Count (2),
    Input,
End Collection,
Usage Page (Desktop),       ; Generic desktop controls (01h)
Usage (Keyboard),           ; Keyboard (06h, application collection)
Collection (Application),
    Report ID (2),
    Usage Page (Keyboard),  ; Keyboard/keypad (07h)
    Usage Minimum (None),   ; No event (00h, selector)
    Usage Maximum (FFh),
    Logical Minimum (0),
    Logical Maximum (255),
    Report Size (8),
    Report Count (10),
    Input,
End Collection
