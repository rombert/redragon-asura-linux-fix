Usage Page (Consumer),                          ; Consumer (0Ch)
Usage (Consumer Control),                       ; Consumer control (01h, application collection)
Collection (Application),
    Report ID (1),
    Usage Minimum (00h),
    Usage Maximum (0380h),
    Logical Minimum (0),
    Logical Maximum (896),
    Report Count (1),
    Report Size (16),
    Input,
End Collection,
Usage Page (Desktop),                           ; Generic desktop controls (01h)
Usage (Sys Control),                            ; System control (80h, application collection)
Collection (Application),
    Report ID (2),
    Usage Minimum (Sys Power Down),             ; System power down (81h, one-shot control)
    Usage Maximum (Sys Wake Up),                ; System wake up (83h, one-shot control)
    Logical Minimum (0),
    Logical Maximum (1),
    Report Size (1),
    Report Count (3),
    Input (Variable),
    Report Count (5),
    Input (Constant),
End Collection,
Usage Page (FF00h),                             ; FF00h, vendor-defined
Usage (01h),
Collection (Application),
    Report ID (3),
    Usage Minimum (F1h),
    Usage Maximum (F8h),
    Logical Minimum (0),
    Logical Maximum (1),
    Report Size (1),
    Report Count (8),
    Input (Variable),
End Collection,
Usage Page (Desktop),                           ; Generic desktop controls (01h)
Usage (Keyboard),                               ; Keyboard (06h, application collection)
Collection (Application),
    Report ID (4),
    Usage Page (Keyboard),                      ; Keyboard/keypad (07h)
    Usage Minimum (KB Leftcontrol),             ; Keyboard left control (E0h, dynamic value)
    Usage Maximum (KB Right GUI),               ; Keyboard right GUI (E7h, dynamic value)
    Logical Minimum (0),
    Logical Maximum (1),
    Report Size (1),
    Report Count (8),
    Input,
    Report Count (48),
    Report Size (1),
    Logical Minimum (0),
    Logical Maximum (1),
    Usage Page (Keyboard),                      ; Keyboard/keypad (07h)
    Usage Minimum (None),                       ; No event (00h, selector)
    Usage Maximum (KB Lboxbracket And Lbrace),  ; Keyboard [ and { (2Fh, selector)
    Input (Variable),
End Collection,
Usage Page (Desktop),                           ; Generic desktop controls (01h)
Usage (Keyboard),                               ; Keyboard (06h, application collection)
Collection (Application),
    Report ID (5),
    Report Count (56),
    Report Size (1),
    Logical Minimum (0),
    Logical Maximum (1),
    Usage Page (Keyboard),                      ; Keyboard/keypad (07h)
    Usage Minimum (KB Rboxbracket And Rbrace),  ; Keyboard ] and } (30h, selector)
    Usage Maximum (KP Equals),                  ; Keypad = (67h, selector)
    Input (Variable),
End Collection,
Usage Page (Desktop),                           ; Generic desktop controls (01h)
Usage (Keyboard),                               ; Keyboard (06h, application collection)
Collection (Application),
    Report ID (6),
    Report Count (56),
    Report Size (1),
    Logical Minimum (0),
    Logical Maximum (1),
    Usage Page (Keyboard),                      ; Keyboard/keypad (07h)
    Usage Minimum (KB F13),                     ; Keyboard F13 (68h, selector)
    Usage Maximum (KB Separator),               ; Keyboard Separator (9Fh, selector)
    Input (Variable),
End Collection
