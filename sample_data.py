# sample_data.py

TRANSACTIONS = [
    # Clean Matches (~12 pairs)
    {"id": "tx_01", "date": "2026-07-01", "amount": 15000.00, "description": "PLDT INC BILL PAYMENT", "source": "GCash"},
    {"id": "tx_02", "date": "2026-07-02", "amount": 4500.25, "description": "MERALCO ONLINE PYMT", "source": "Bank"},
    {"id": "tx_03", "date": "2026-07-03", "amount": 12500.00, "description": "GLOBE TELECOM BILL", "source": "Maya"},
    {"id": "tx_04", "date": "2026-07-04", "amount": 850.00, "description": "GRAB CAR MANILA", "source": "GCash"},
    {"id": "tx_05", "date": "2026-07-05", "amount": 3200.00, "description": "LALAMOVE CORP DELIVERY", "source": "Bank"},
    {"id": "tx_06", "date": "2026-07-05", "amount": 24500.00, "description": "AYALA LAND LEASE PAYMENT", "source": "Bank"},
    {"id": "tx_07", "date": "2026-07-06", "amount": 180.00, "description": "7-ELEVEN STORE CONV", "source": "GCash"},
    {"id": "tx_08", "date": "2026-07-06", "amount": 6200.50, "description": "SM SUPERMARKET FOOD", "source": "Bank"},
    {"id": "tx_09", "date": "2026-07-07", "amount": 950.00, "description": "ANGKAS RIDE PYMT", "source": "Maya"},
    {"id": "tx_10", "date": "2026-07-08", "amount": 1500.00, "description": "NATIONAL BOOK STORE", "source": "GCash"},
    {"id": "tx_11", "date": "2026-07-09", "amount": 3500.00, "description": "CONVERGE ICT PYMT", "source": "Bank"},
    {"id": "tx_12", "date": "2026-07-09", "amount": 2200.00, "description": "SHELL PETROLEUM FILLUP", "source": "Bank"},

    # Duplicate Transactions (2-3 transactions)
    # tx_13 is a duplicate payment of tx_04 (Grab, same amount, 1 day later, different transaction ID)
    {"id": "tx_13", "date": "2026-07-05", "amount": 850.00, "description": "GRAB CAR MANILA", "source": "GCash"},
    # tx_14 is a duplicate payment of tx_07 (7-Eleven, same amount, 1 day later, different transaction ID)
    {"id": "tx_14", "date": "2026-07-07", "amount": 180.00, "description": "7-ELEVEN STORE CONV", "source": "GCash"},

    # Mismatches (2-3 pairs with amount differences, e.g. due to fees)
    # tx_15 matches inv_15 but has an extra 15.00 GCash cash-in/convenience fee
    {"id": "tx_15", "date": "2026-07-08", "amount": 5015.00, "description": "MAYA MERCHANT PYMT", "source": "GCash"},
    # tx_16 matches inv_16 but has an extra 50.00 bank transfer fee included
    {"id": "tx_16", "date": "2026-07-09", "amount": 10050.00, "description": "JOLLIBEE FOODS CORP", "source": "Bank"},
    # tx_17 matches inv_17 but is short by 3.00 (discount or adjustments)
    {"id": "tx_17", "date": "2026-07-10", "amount": 247.00, "description": "SHOPEE PH DELIVERY", "source": "Maya"},

    # Missing Invoices (2-3 transactions with NO matching invoice)
    {"id": "tx_18", "date": "2026-07-10", "amount": 50000.00, "description": "CASH WITHDRAWAL OVER THE COUNTER", "source": "Bank"},
    {"id": "tx_19", "date": "2026-07-11", "amount": 1200.00, "description": "STARBUCKS COFFEE MAKATI", "source": "GCash"},
    {"id": "tx_20", "date": "2026-07-11", "amount": 450.00, "description": "NETFLIX PHILIPPINES", "source": "Maya"}
]

INVOICES = [
    # Clean Matches
    {"id": "inv_01", "date": "2026-07-01", "amount": 15000.00, "supplier": "PLDT Inc.", "reference_number": "INV-PLDT-889"},
    {"id": "inv_02", "date": "2026-07-02", "amount": 4500.25, "supplier": "Meralco", "reference_number": "INV-MER-102"},
    {"id": "inv_03", "date": "2026-07-03", "amount": 12500.00, "supplier": "Globe Telecom", "reference_number": "INV-GLOBE-454"},
    {"id": "inv_04", "date": "2026-07-04", "amount": 850.00, "supplier": "Grab Philippines", "reference_number": "INV-GRAB-001"},
    {"id": "inv_05", "date": "2026-07-05", "amount": 3200.00, "supplier": "Lalamove", "reference_number": "INV-LALA-330"},
    {"id": "inv_06", "date": "2026-07-05", "amount": 24500.00, "supplier": "Ayala Land Inc.", "reference_number": "INV-ALI-998"},
    {"id": "inv_07", "date": "2026-07-06", "amount": 180.00, "supplier": "7-Eleven Store", "reference_number": "INV-711-502"},
    {"id": "inv_08", "date": "2026-07-06", "amount": 6200.50, "supplier": "SM Supermarket", "reference_number": "INV-SM-203"},
    {"id": "inv_09", "date": "2026-07-07", "amount": 950.00, "supplier": "Angkas", "reference_number": "INV-ANG-774"},
    {"id": "inv_10", "date": "2026-07-08", "amount": 1500.00, "supplier": "National Book Store", "reference_number": "INV-NBS-109"},
    {"id": "inv_11", "date": "2026-07-09", "amount": 3500.00, "supplier": "Converge ICT Solutions", "reference_number": "INV-CONV-382"},
    {"id": "inv_12", "date": "2026-07-09", "amount": 2200.00, "supplier": "Shell Petroleum", "reference_number": "INV-SHELL-120"},

    # Mismatches (amounts differ slightly)
    {"id": "inv_15", "date": "2026-07-08", "amount": 5000.00, "supplier": "Maya Merchant", "reference_number": "INV-MAYA-607"},
    {"id": "inv_16", "date": "2026-07-09", "amount": 10000.00, "supplier": "Jollibee Foods Corp", "reference_number": "INV-JFC-890"},
    {"id": "inv_17", "date": "2026-07-10", "amount": 250.00, "supplier": "Shopee PH", "reference_number": "INV-SHOPEE-112"},

    # Unmatched Invoices (Invoices with NO matching transaction)
    {"id": "inv_18", "date": "2026-07-10", "amount": 8900.00, "supplier": "Max's Restaurant", "reference_number": "INV-MAX-99"},
    {"id": "inv_19", "date": "2026-07-11", "amount": 1230.00, "supplier": "Mercury Drug", "reference_number": "INV-MERC-04"}
]
