"""
Specialized invoice and receipt extraction module.
"""

import json
from typing import Dict, Any, Optional
from ..text_extractor import TextExtractor


class InvoiceExtractor:
    """Extract structured data from invoices and receipts."""

    def __init__(self, provider: str = None, api_key: str = None):
        """
        Initialize InvoiceExtractor.

        Args:
            provider: LLM provider name
            api_key: API key for the provider
        """
        self.extractor = TextExtractor(provider=provider, api_key=api_key)

    def extract(self, invoice_text: str) -> Dict[str, Any]:
        """
        Extract structured information from invoice text.

        Args:
            invoice_text: Raw invoice text

        Returns:
            Dictionary with extracted invoice data
        """
        schema = {
            "invoice_number": "string",
            "invoice_date": "string (YYYY-MM-DD format)",
            "due_date": "string (YYYY-MM-DD format)",
            "vendor": {
                "name": "string",
                "address": "string",
                "phone": "string",
                "email": "string",
            },
            "customer": {
                "name": "string",
                "address": "string",
                "phone": "string",
                "email": "string",
            },
            "line_items": [
                {
                    "description": "string",
                    "quantity": "number",
                    "unit_price": "number",
                    "total": "number",
                }
            ],
            "subtotal": "number",
            "tax": "number",
            "tax_rate": "number (percentage)",
            "total": "number",
            "currency": "string (ISO code like USD, EUR)",
            "payment_terms": "string",
            "payment_method": "string",
            "notes": "string",
        }

        return self.extractor.extract_structured_data(invoice_text, schema)

    def extract_line_items(self, invoice_text: str) -> list:
        """
        Extract only line items from invoice.

        Args:
            invoice_text: Raw invoice text

        Returns:
            List of line items
        """
        prompt = f"""Extract all line items from this invoice.

Invoice:
{invoice_text}

Return ONLY a JSON array of line items with:
- description
- quantity
- unit_price
- total

Format:
[
  {{
    "description": "Item name",
    "quantity": 2,
    "unit_price": 50.00,
    "total": 100.00
  }}
]"""

        response = self.extractor.provider.complete(
            prompt, temperature=0.1, max_tokens=1500
        )

        try:
            items = json.loads(response)
            return items
        except json.JSONDecodeError:
            if "```json" in response:
                json_start = response.find("```json") + 7
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            elif "```" in response:
                json_start = response.find("```") + 3
                json_end = response.find("```", json_start)
                json_str = response[json_start:json_end].strip()
                return json.loads(json_str)
            else:
                return []

    def validate_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate extracted invoice data for completeness and accuracy.

        Args:
            invoice_data: Extracted invoice data

        Returns:
            Validation results with warnings and errors
        """
        validation_result = {"valid": True, "warnings": [], "errors": []}

        # Check required fields
        required_fields = ["invoice_number", "total", "vendor", "customer"]
        for field in required_fields:
            if field not in invoice_data or not invoice_data[field]:
                validation_result["errors"].append(f"Missing required field: {field}")
                validation_result["valid"] = False

        # Validate totals
        if "line_items" in invoice_data and invoice_data["line_items"]:
            calculated_subtotal = sum(
                item.get("total", 0) for item in invoice_data["line_items"]
            )
            reported_subtotal = invoice_data.get("subtotal", 0)

            if abs(calculated_subtotal - reported_subtotal) > 0.01:
                validation_result["warnings"].append(
                    f"Subtotal mismatch: calculated {calculated_subtotal}, "
                    f"reported {reported_subtotal}"
                )

        # Validate tax calculation
        if "subtotal" in invoice_data and "tax_rate" in invoice_data:
            calculated_tax = invoice_data["subtotal"] * (
                invoice_data["tax_rate"] / 100
            )
            reported_tax = invoice_data.get("tax", 0)

            if abs(calculated_tax - reported_tax) > 0.01:
                validation_result["warnings"].append(
                    f"Tax calculation mismatch: calculated {calculated_tax}, "
                    f"reported {reported_tax}"
                )

        # Validate total
        if "subtotal" in invoice_data and "tax" in invoice_data:
            calculated_total = invoice_data["subtotal"] + invoice_data["tax"]
            reported_total = invoice_data.get("total", 0)

            if abs(calculated_total - reported_total) > 0.01:
                validation_result["errors"].append(
                    f"Total mismatch: calculated {calculated_total}, "
                    f"reported {reported_total}"
                )
                validation_result["valid"] = False

        return validation_result

    def extract_and_validate(self, invoice_text: str) -> Dict[str, Any]:
        """
        Extract and validate invoice data in one step.

        Args:
            invoice_text: Raw invoice text

        Returns:
            Dictionary with extracted data and validation results
        """
        invoice_data = self.extract(invoice_text)
        validation = self.validate_invoice(invoice_data)

        return {"data": invoice_data, "validation": validation}
