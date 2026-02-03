"""
Specialized resume/CV parsing module.
"""

import json
from typing import Dict, Any, List
from ..text_extractor import TextExtractor


class ResumeExtractor:
    """Extract structured data from resumes and CVs."""

    def __init__(self, provider: str = None, api_key: str = None):
        """
        Initialize ResumeExtractor.

        Args:
            provider: LLM provider name
            api_key: API key for the provider
        """
        self.extractor = TextExtractor(provider=provider, api_key=api_key)

    def extract(self, resume_text: str) -> Dict[str, Any]:
        """
        Extract structured information from resume text.

        Args:
            resume_text: Raw resume text

        Returns:
            Dictionary with extracted resume data
        """
        schema = {
            "personal_info": {
                "name": "string",
                "email": "string",
                "phone": "string",
                "location": "string (city, state/country)",
                "linkedin": "string (URL)",
                "github": "string (URL)",
                "website": "string (URL)",
            },
            "summary": "string (professional summary/objective)",
            "work_experience": [
                {
                    "company": "string",
                    "position": "string",
                    "location": "string",
                    "start_date": "string (MM/YYYY)",
                    "end_date": "string (MM/YYYY or 'Present')",
                    "description": "string",
                    "achievements": ["string"],
                }
            ],
            "education": [
                {
                    "institution": "string",
                    "degree": "string",
                    "field_of_study": "string",
                    "location": "string",
                    "graduation_date": "string (MM/YYYY)",
                    "gpa": "string (optional)",
                    "honors": ["string"],
                }
            ],
            "skills": {
                "technical": ["string"],
                "languages": ["string"],
                "tools": ["string"],
                "soft_skills": ["string"],
            },
            "certifications": [
                {
                    "name": "string",
                    "issuing_organization": "string",
                    "date": "string (MM/YYYY)",
                    "credential_id": "string (optional)",
                }
            ],
            "projects": [
                {
                    "name": "string",
                    "description": "string",
                    "technologies": ["string"],
                    "url": "string (optional)",
                }
            ],
            "awards": ["string"],
            "publications": ["string"],
            "languages": [{"language": "string", "proficiency": "string"}],
        }

        return self.extractor.extract_structured_data(resume_text, schema)

    def extract_contact_info(self, resume_text: str) -> Dict[str, str]:
        """
        Extract only contact information from resume.

        Args:
            resume_text: Raw resume text

        Returns:
            Dictionary with contact information
        """
        prompt = f"""Extract contact information from this resume.

Resume:
{resume_text}

Return ONLY a JSON object with these fields (use null for missing fields):
{{
  "name": "Full Name",
  "email": "email@example.com",
  "phone": "+1-234-567-8900",
  "location": "City, State",
  "linkedin": "https://linkedin.com/in/username",
  "github": "https://github.com/username",
  "website": "https://example.com"
}}"""

        response = self.extractor.provider.complete(
            prompt, temperature=0.1, max_tokens=500
        )

        try:
            contact_info = json.loads(response)
            return contact_info
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
                return {}

    def extract_skills(self, resume_text: str) -> Dict[str, List[str]]:
        """
        Extract only skills from resume.

        Args:
            resume_text: Raw resume text

        Returns:
            Dictionary categorizing different types of skills
        """
        prompt = f"""Extract all skills from this resume, categorized by type.

Resume:
{resume_text}

Return ONLY a JSON object:
{{
  "technical": ["Python", "Java", "etc"],
  "languages": ["English", "Spanish", "etc"],
  "tools": ["Git", "Docker", "etc"],
  "soft_skills": ["Leadership", "Communication", "etc"]
}}"""

        response = self.extractor.provider.complete(
            prompt, temperature=0.1, max_tokens=1000
        )

        try:
            skills = json.loads(response)
            return skills
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
                return {
                    "technical": [],
                    "languages": [],
                    "tools": [],
                    "soft_skills": [],
                }

    def match_job_description(
        self, resume_text: str, job_description: str
    ) -> Dict[str, Any]:
        """
        Analyze how well a resume matches a job description.

        Args:
            resume_text: Raw resume text
            job_description: Job description text

        Returns:
            Dictionary with match analysis
        """
        prompt = f"""Analyze how well this resume matches the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return a JSON object with:
{{
  "match_score": 0-100,
  "matching_skills": ["skill1", "skill2"],
  "missing_skills": ["skill3", "skill4"],
  "relevant_experience": ["experience1", "experience2"],
  "strengths": ["strength1", "strength2"],
  "gaps": ["gap1", "gap2"],
  "recommendations": ["recommendation1", "recommendation2"],
  "summary": "Brief analysis of the match"
}}"""

        response = self.extractor.provider.complete(
            prompt, temperature=0.1, max_tokens=1500
        )

        try:
            match_analysis = json.loads(response)
            return match_analysis
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
                return {"error": "Failed to parse match analysis"}

    def generate_summary(self, resume_data: Dict[str, Any]) -> str:
        """
        Generate a professional summary from extracted resume data.

        Args:
            resume_data: Extracted resume data

        Returns:
            Professional summary text
        """
        prompt = f"""Based on this resume data, write a compelling 2-3 sentence professional summary:

{json.dumps(resume_data, indent=2)}

Write a concise, impactful professional summary that highlights key qualifications and value proposition."""

        return self.extractor.provider.complete(
            prompt, temperature=0.3, max_tokens=300
        )
