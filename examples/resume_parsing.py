"""
Example: Resume Parsing

This example demonstrates how to extract structured data from resumes.
"""

from src.extractors.resume_extractor import ResumeExtractor
import json


def main():
    # Initialize the resume extractor
    extractor = ResumeExtractor()

    # Example resume
    resume_text = """
    SARAH CHEN
    Full Stack Software Engineer
    
    Email: sarah.chen@email.com
    Phone: +1 (555) 234-5678
    Location: Seattle, WA
    LinkedIn: linkedin.com/in/sarahchen
    GitHub: github.com/sarahchen
    Portfolio: sarahchen.dev
    
    PROFESSIONAL SUMMARY
    Experienced Full Stack Software Engineer with 6+ years of expertise in building 
    scalable web applications. Proficient in modern JavaScript frameworks, cloud 
    technologies, and agile methodologies. Passionate about creating elegant solutions 
    to complex problems and mentoring junior developers.
    
    WORK EXPERIENCE
    
    Senior Software Engineer | Tech Innovations Inc. | Seattle, WA
    March 2021 - Present
    - Led development of microservices architecture serving 2M+ daily active users
    - Reduced API response time by 40% through optimization and caching strategies
    - Mentored team of 5 junior developers on best practices and code quality
    - Implemented CI/CD pipelines reducing deployment time from 2 hours to 15 minutes
    - Technologies: React, Node.js, PostgreSQL, AWS, Docker, Kubernetes
    
    Software Engineer | Digital Solutions Corp | San Francisco, CA  
    June 2018 - February 2021
    - Built and maintained customer-facing web applications used by 500K+ users
    - Collaborated with UX designers to implement responsive, accessible interfaces
    - Developed RESTful APIs and integrated third-party payment systems
    - Participated in code reviews and contributed to engineering blog
    - Technologies: Vue.js, Python, MongoDB, AWS, Redis
    
    Junior Developer | StartUp Ventures | San Francisco, CA
    August 2017 - May 2018
    - Contributed to development of MVP for SaaS platform
    - Fixed bugs and implemented new features based on user feedback
    - Wrote unit tests achieving 85% code coverage
    - Technologies: Angular, Django, MySQL
    
    EDUCATION
    
    Bachelor of Science in Computer Science | Stanford University | Stanford, CA
    Graduated: May 2017 | GPA: 3.8/4.0
    - Dean's List all semesters
    - Senior Project: Built AI-powered recommendation system
    
    TECHNICAL SKILLS
    
    Languages: JavaScript, TypeScript, Python, Java, SQL, HTML, CSS
    Frontend: React, Vue.js, Angular, Next.js, Redux, Tailwind CSS
    Backend: Node.js, Express, Django, Flask, FastAPI
    Databases: PostgreSQL, MongoDB, MySQL, Redis
    Cloud & DevOps: AWS (EC2, S3, Lambda, RDS), Docker, Kubernetes, Jenkins, GitHub Actions
    Tools: Git, JIRA, Figma, Postman
    
    CERTIFICATIONS
    
    AWS Certified Solutions Architect - Associate | Amazon Web Services | June 2022
    Certified Kubernetes Application Developer (CKAD) | CNCF | March 2023
    
    PROJECTS
    
    Open Source Contributor - React Native Framework
    - Contributed bug fixes and documentation improvements
    - GitHub: github.com/facebook/react-native
    
    Personal Finance Tracker
    - Built full-stack application helping users manage expenses
    - Tech Stack: React, Node.js, PostgreSQL, Chart.js
    - Live: financetracker-demo.com
    
    AWARDS & ACHIEVEMENTS
    - Employee of the Quarter, Q3 2022 - Tech Innovations Inc.
    - Hackathon Winner, TechCrunch Disrupt 2020
    - Top 1% contributor on Stack Overflow (15K+ reputation)
    
    LANGUAGES
    English - Native
    Mandarin Chinese - Professional working proficiency
    Spanish - Basic conversational
    """

    # Example 1: Full resume extraction
    print("=" * 60)
    print("Example 1: Full Resume Extraction")
    print("=" * 60)

    resume_data = extractor.extract(resume_text)
    print("\nExtracted Resume Data:")
    print(json.dumps(resume_data, indent=2))

    # Example 2: Contact info only
    print("\n" + "=" * 60)
    print("Example 2: Extract Contact Information Only")
    print("=" * 60)

    contact_info = extractor.extract_contact_info(resume_text)
    print("\nContact Information:")
    print(json.dumps(contact_info, indent=2))

    # Example 3: Skills extraction
    print("\n" + "=" * 60)
    print("Example 3: Extract Skills Only")
    print("=" * 60)

    skills = extractor.extract_skills(resume_text)
    print("\nExtracted Skills:")
    print(json.dumps(skills, indent=2))

    # Example 4: Job matching
    print("\n" + "=" * 60)
    print("Example 4: Match Resume to Job Description")
    print("=" * 60)

    job_description = """
    Senior Full Stack Engineer
    
    We're looking for an experienced Full Stack Engineer to join our team.
    
    Requirements:
    - 5+ years of experience with React and Node.js
    - Strong knowledge of AWS cloud services
    - Experience with Docker and Kubernetes
    - Excellent problem-solving skills
    - Experience mentoring junior developers
    - Bachelor's degree in Computer Science or related field
    
    Nice to have:
    - Experience with TypeScript
    - Knowledge of GraphQL
    - Contributions to open source projects
    - AWS certifications
    """

    match_analysis = extractor.match_job_description(resume_text, job_description)
    print("\nJob Match Analysis:")
    print(json.dumps(match_analysis, indent=2))

    # Example 5: Generate professional summary
    print("\n" + "=" * 60)
    print("Example 5: Generate Professional Summary")
    print("=" * 60)

    summary = extractor.generate_summary(resume_data)
    print(f"\nGenerated Summary:\n{summary}")


if __name__ == "__main__":
    main()
