#!/usr/bin/env python3
"""
Test script to verify PDF reading functionality
"""

import os
from cover_letter_generator import CoverLetterGenerator

def test_pdf_reading():
    """Test if the program can read PDF content properly."""
    print("Testing PDF reading functionality...")
    print("=" * 50)
    
    try:
        # Initialize the generator
        generator = CoverLetterGenerator()
        
        # Test reading the default resume PDF
        print("Testing PDF resume reading...")
        resume_content = generator._read_file_or_text("Artin_Majd_CV.pdf")
        
        print(f"✅ Successfully read PDF resume")
        print(f"📄 Content length: {len(resume_content)} characters")
        print(f"📝 First 200 characters:")
        print("-" * 30)
        print(resume_content[:2000] + "..." if len(resume_content) > 200 else resume_content)
        print("-" * 30)
        
        # Test reading the job description text file
        print("\nTesting text file reading...")
        job_content = generator._read_file_or_text("job_description.txt")
        
        print(f"✅ Successfully read job description")
        print(f"📄 Content length: {len(job_content)} characters")
        print(f"📝 First 200 characters:")
        print("-" * 30)
        print(job_content[:200] + "..." if len(job_content) > 200 else job_content)
        print("-" * 30)
        
        
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_pdf_reading()
