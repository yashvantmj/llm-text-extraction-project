"""
Example: Invoice Processing

This example demonstrates how to extract structured data from invoices.
"""

from src.extractors.invoice_extractor import InvoiceExtractor
import json


def main():
    # Initialize the invoice extractor
    extractor = InvoiceExtractor()

    # Example 1: Simple invoice
    print("=" * 60)
    print("Example 1: Simple Invoice Extraction")
    print("=" * 60)

    invoice1 = """
    INVOICE #INV-2024-001
    
    Date: January 15, 2024
    Due Date: February 15, 2024
    
    From:
    Tech Solutions Inc.
    123 Main Street
    San Francisco, CA 94102
    Phone: (555) 123-4567
    Email: billing@techsolutions.com
    
    To:
    Acme Corporation
    456 Business Ave
    New York, NY 10001
    Phone: (555) 987-6543
    Email: accounts@acmecorp.com
    
    Items:
    1. Web Development Services - 40 hours @ $150/hr = $6,000.00
    2. UI/UX Design - 20 hours @ $120/hr = $2,400.00
    3. Project Management - 10 hours @ $100/hr = $1,000.00
    
    Subtotal: $9,400.00
    Tax (8.5%): $799.00
    Total: $10,199.00
    
    Payment Terms: Net 30
    Payment Method: Bank Transfer or Check
    
    Notes: Thank you for your business!
    """

    invoice_data = extractor.extract(invoice1)
    print("\nExtracted Invoice Data:")
    print(json.dumps(invoice_data, indent=2))

    # Example 2: Extract and validate
    print("\n" + "=" * 60)
    print("Example 2: Invoice Extraction with Validation")
    print("=" * 60)

    invoice2 = """
    INVOICE #2024-0042
    
    Date: March 10, 2024
    Due: April 10, 2024
    
    VENDOR:
    Premium Office Supplies
    789 Commerce Blvd
    Chicago, IL 60601
    supplies@premiumoffice.com
    
    BILL TO:
    StartUp Co.
    321 Innovation Drive
    Austin, TX 78701
    
    DESCRIPTION                          QTY    PRICE    TOTAL
    Ergonomic Office Chairs               5    $299.99  $1,499.95
    Standing Desks                        3    $599.99  $1,799.97
    Wireless Keyboards                   10     $79.99    $799.90
    4K Monitors                           8    $449.99  $3,599.92
    
    Subtotal:                                            $7,699.74
    Sales Tax (6.25%):                                     $481.23
    Shipping:                                               $50.00
    TOTAL DUE:                                           $8,230.97
    
    Payment Terms: Due upon receipt
    """

    result = extractor.extract_and_validate(invoice2)
    print("\nExtracted Data:")
    print(json.dumps(result["data"], indent=2))
    print("\nValidation Results:")
    print(json.dumps(result["validation"], indent=2))

    # Example 3: Line items only
    print("\n" + "=" * 60)
    print("Example 3: Extract Line Items Only")
    print("=" * 60)

    invoice3 = """
    ORDER SUMMARY
    
    Product: Cloud Storage Subscription (1TB) - $99.99
    Product: Email Service (50 accounts) - $49.99  
    Product: Video Conferencing (Pro Plan) - $149.99
    Product: Document Management System - $199.99
    
    Total: $499.96
    """

    line_items = extractor.extract_line_items(invoice3)
    print("\nExtracted Line Items:")
    print(json.dumps(line_items, indent=2))

    # Example 4: International invoice
    print("\n" + "=" * 60)
    print("Example 4: International Invoice (EUR)")
    print("=" * 60)

    invoice4 = """
    RECHNUNG / INVOICE
    Nr: 2024-DE-156
    
    Datum: 20. Januar 2024
    Fällig: 20. Februar 2024
    
    Von:
    Deutsche Tech GmbH
    Hauptstraße 45
    10115 Berlin, Deutschland
    Tel: +49 30 12345678
    
    An:
    Global Enterprises Ltd
    Business Park 12
    London, UK
    
    Leistungen / Services:
    Software Entwicklung    100 Std.    €120/Std    €12,000.00
    Beratung / Consulting    30 Std.     €150/Std     €4,500.00
    
    Zwischensumme / Subtotal:                        €16,500.00
    MwSt. 19% / VAT 19%:                              €3,135.00
    Gesamtbetrag / Total:                            €19,635.00
    
    Zahlungsbedingungen: 30 Tage netto
    """

    invoice_data = extractor.extract(invoice4)
    print("\nExtracted Invoice Data:")
    print(json.dumps(invoice_data, indent=2))


if __name__ == "__main__":
    main()
