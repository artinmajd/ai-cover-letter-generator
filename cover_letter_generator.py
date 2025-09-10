"""
AI-Powered Cover Letter Generator using GPT-4o
"""

import os
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv
import PyPDF2


class CoverLetterGenerator:
    """Generates cover letters using GPT-4o based on resume and job description."""
    
    def __init__(self, contact_info: Optional[dict] = None):
        """
        Initialize the cover letter generator with OpenAI client.
        
        Args:
            contact_info: Dictionary with 'email', 'phone', 'linkedin' keys.
                         If None, will try to load from environment variables.
        """
        # Load environment variables
        load_dotenv()
        
        # Get OpenAI API key from environment
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key)
        
        # Default model
        self.default_model = "gpt-4o"
        
        # Set up contact information
        self.contact_info = self._setup_contact_info(contact_info)
    
    def _setup_contact_info(self, contact_info: Optional[dict]) -> dict:
        """
        Set up contact information from parameters or environment variables.
        
        Args:
            contact_info: Optional dictionary with contact details
            
        Returns:
            Dictionary with contact information
        """
        if contact_info:
            return contact_info
        
        # Try to load from environment variables
        env_contact = {
            'email': os.getenv('CONTACT_EMAIL', 'your.email@example.com'),
            'phone': os.getenv('CONTACT_PHONE', '+1 (XXX) XXX-XXXX'),
            'linkedin': os.getenv('CONTACT_LINKEDIN', 'linkedin.com/in/your-profile'),
            'website': os.getenv('CONTACT_WEBSITE', 'www.yourwebsite.com')
        }
        
        return env_contact
    
    def generate_with_ai(
        self, 
        resume: str, 
        job_description: str, 
        model: Optional[str] = None
    ) -> str:
        """
        Generate a cover letter using GPT-4o based on resume and job description.
        
        Args:
            resume: Resume text or file path
            job_description: Job description text or file path
            model: OpenAI model to use
            
        Returns:
            Generated cover letter text
        """
        # Read files if paths are provided
        resume_text = self._read_file_or_text(resume)
        job_desc_text = self._read_file_or_text(job_description)
        
        # Use default model if none specified
        model = model or self.default_model
        
        # Create the prompt for GPT-4o
        prompt = self._create_prompt(resume_text, job_desc_text)
        
        try:
            # Generate cover letter using OpenAI API
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert cover letter writer who creates natural, humanized, and conversational cover letters."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            cover_letter = response.choices[0].message.content.strip()
            return cover_letter
            
        except Exception as e:
            raise Exception(f"Error generating cover letter with OpenAI: {str(e)}")
    
    def _read_file_or_text(self, input_data: str) -> str:
        """
        Read content from file if path is provided, otherwise return the text.
        Supports PDF files and text files.
        
        Args:
            input_data: File path or text content
            
        Returns:
            Content as string
        """
        if os.path.isfile(input_data):
            try:
                # Check if it's a PDF file
                if input_data.lower().endswith('.pdf'):
                    return self._read_pdf_file(input_data)
                else:
                    # Read as text file
                    with open(input_data, 'r', encoding='utf-8') as f:
                        return f.read()
            except Exception as e:
                raise Exception(f"Error reading file {input_data}: {str(e)}")
        else:
            return input_data
    
    def _read_pdf_file(self, pdf_path: str) -> str:
        """
        Read text content from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text content
        """
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except ImportError:
            raise Exception("PyPDF2 is required to read PDF files. Please install it with: pip install PyPDF2")
        except Exception as e:
            raise Exception(f"Error reading PDF file {pdf_path}: {str(e)}")
    
    def _create_prompt(self, resume: str, job_description: str) -> str:
        """
        Create a comprehensive prompt for GPT-4o using the user's specific instructions.
        
        Args:
            resume: Resume content
            job_description: Job description content
            
        Returns:
            Formatted prompt string
        """
        prompt = f"""Write a great cover letter for this job description. Use what you already know from my resume to highlight my most relevant experiences and skills. Make sure the tone is very humanized, natural, and conversational rather than sounding like a typical AI-generated text. Avoid em dashes and odd punctuation. Keep it professional but approachable, with a strong narrative that shows why I'm a good fit. Do not use any placeholders or bracketed fields of any kind (no [], <>, {{}}, ALL CAPS prompts like INSERT/ADD HERE, or 'to be filled later'). Provide fully realized, final content with no TODOs or TBDs.

End the letter with the following four separate lines:
Email: {self.contact_info['email']}
Phone: {self.contact_info['phone']}
LinkedIn: {self.contact_info['linkedin']}
Website: {self.contact_info['website']}

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Please generate the complete cover letter text only, without any additional explanations or formatting instructions.
**IMPORTANT**
- NO em dashes
- Do not emphsize on my education and instead try to make it sound like I'm a good fit for the job using my experiences and skills.
- Usually the companies don't care about my GPA.
- If in the job description you detect a certain challenge they are facing, try to highlight how my experiences and skills can help them overcome that challenge.
"""

        return prompt
    
    def set_model(self, model: str):
        """Set the default OpenAI model to use."""
        self.default_model = model
