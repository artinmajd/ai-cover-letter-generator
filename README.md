# AI-Powered Cover Letter Generator

A Python tool that uses GPT-4o to generate personalized, natural cover letters based on your resume and job descriptions.

## Features

- 🤖 **AI-Powered Generation**: Uses GPT-4o to create compelling, personalized cover letters
- 📄 **Resume Integration**: Analyzes your resume to match it with job requirements
- 🎯 **Job Description Analysis**: Understands job requirements and tailors the cover letter accordingly
- 💬 **Natural Tone**: Generates humanized, conversational cover letters that don't sound AI-generated
- 💾 **Flexible Input**: Accepts both text and file inputs for resume and job descriptions
- 📤 **Multiple Outputs**: Display on console or save to file
- 📋 **Smart Defaults**: Automatically uses your default resume and job description if none specified

## Prerequisites

- Python 3.7+
- OpenAI API key (get one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CoverLetterGenerator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. Place your default files in the project root:
   ```bash
   # The tool will automatically use:
   # - Artin_Majd_CV.pdf (default resume)
   # - job_description.txt (default job description)
   ```

## Configuration

Create a `.env` file in your project root with your OpenAI API key and contact information:

```bash
OPENAI_API_KEY=your_actual_api_key_here

# Your contact information (will be added to generated cover letters)
CONTACT_EMAIL=your.email@example.com
CONTACT_PHONE=+1 (XXX) XXX-XXXX  
CONTACT_LINKEDIN=linkedin.com/in/your-profile
```

## Usage

### Simplest Usage (with all defaults)

Generate a cover letter using your default resume and job description:

```bash
python main.py
```

### Specify Custom Job Description

Generate a cover letter with a custom job description:

```bash
python main.py "Custom job description text here"
```

### Specify Custom Resume

Generate a cover letter with a custom resume:

```bash
python main.py "Your resume content here" "Job description text here"
```

### Using Files

Generate a cover letter from resume and job description files:

```bash
python main.py resume.txt job_description.txt
```

### Specify Output File

Save the generated cover letter to a file:

```bash
python main.py --output my_cover_letter.txt
```

### Choose AI Model

Select a different OpenAI model:

```bash
python main.py --model gpt-4
```

### Help

Get help on available options:

```bash
python main.py --help
```

## Examples

```bash
# Use all defaults (Artin_Majd_CV.pdf + job_description.txt)
python main.py

# Use default resume with custom job description
python main.py "Senior Python Developer position requiring Django and AWS skills"

# Use custom resume with default job description
python main.py "Custom resume text here"

# Use custom resume and job description
python main.py "Experienced Python developer with 5 years in web development..." "Senior Software Engineer position requiring Python, Django, and AWS skills"

# Use custom resume file with default job description
python main.py custom_resume.txt

# Use custom files
python main.py custom_resume.txt custom_job.txt

# Generate and save to file
python main.py --output cover_letter.txt

# Use a different model
python main.py --model gpt-4
```

## How It Works

1. **Input Processing**: 
   - Automatically reads your default resume (`Artin_Majd_CV.pdf`) if no resume is specified
   - Automatically reads your default job description (`job_description.txt`) if no job description is specified
   - Supports both PDF and text files
2. **AI Analysis**: GPT-4o analyzes both documents to understand:
   - Your skills, experience, and qualifications
   - Job requirements and company needs
   - How to best match your profile to the position
3. **Cover Letter Generation**: Creates a personalized, compelling cover letter that:
   - Highlights relevant experience from your resume
   - Addresses specific job requirements
   - Maintains a natural, conversational tone
   - Avoids AI-generated language patterns
   - Is tailored to the specific company and role

## Project Structure

- `main.py` - Command-line interface
- `cover_letter_generator.py` - AI-powered cover letter generation logic
- `requirements.txt` - Python dependencies
- `env.example` - Environment variables template  
- `.env` - Your personal environment configuration (not tracked in git)
- Default files (not tracked in git):
  - Your resume file (automatically used if no resume specified)
  - `job_description.txt` - Default job description (automatically used if no job description specified)

## Customization

- **AI Prompts**: Customize the prompt in `cover_letter_generator.py`
- **Model Settings**: Adjust temperature, max tokens, and other parameters
- **Default Files**: Change the default resume and job description files in `main.py`

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `.env` file contains the correct `OPENAI_API_KEY`
2. **Contact Information**: Make sure to update the contact information in your `.env` file (CONTACT_EMAIL, CONTACT_PHONE, CONTACT_LINKEDIN)
3. **Rate Limits**: If you hit OpenAI rate limits, wait a moment and try again
4. **File Encoding**: Ensure your resume and job description files use UTF-8 encoding
5. **PDF Reading**: Ensure PyPDF2 is installed for PDF resume support
6. **Missing Default Files**: Ensure your resume and job description files exist in the project root

### Getting Help

- Check that your OpenAI API key is valid and has sufficient credits
- Ensure your virtual environment is activated
- Verify all dependencies are installed correctly
- Make sure default files exist in the project root if using defaults

## Future Enhancements

- Resume parsing and analysis
- Multiple output formats (PDF, DOCX)
- Cover letter quality scoring
- Integration with job boards
- Batch processing for multiple applications
- Custom prompt templates

## License

MIT License
