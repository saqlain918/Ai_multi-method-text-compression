## AI Text Compression Suite

A Python-based framework for experimenting with advanced text compression techniques. Includes both rule-based and AI-driven methods to reduce document length while preserving meaning, context, and essential information.

## What it does

- Reduces text size while maintaining core meaning
- Offers multiple compression approaches for different use cases
- Provides both traditional and AI-powered compression methods
- Enables experimentation with various compression strategies
- Supports staged compression with progressive reduction
- Ideal for summarization and storage-efficient applications

## Features

- Lexical Compression: Removes stopwords and redundant words
- Semantic Compression: Compresses text while preserving meaning
- Task-Oriented Compression: Compresses text for specific use cases
- Map-Reduce Compression: Chunk-wise compression and merging
- Latent Compression: Extracts and compresses latent semantic concepts
- Iterative Token Reduction: Staged compression (50% → 30% → 15%)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/ai-text-compression-suite.git
   cd ai-text-compression-suite
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Environment setup:
   Copy `.env` to `.env`:
   ```
   cp .env
   ```
   
   Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## How to use

1. Run the main program:
   ```
   python main.py
   ```

2. The program will:
   - Read from `document.txt` by default
   - Allow you to choose a compression technique
   - Display the compressed output in the console

## Example Usage

**Input (document.txt):**
```
Social media has rapidly transformed education by making 
resources more accessible to students and teachers.
```

**Lexical Compression:**
```
Social media rapidly transformed education making resources accessible students teachers
```

**Semantic Compression:**
```
Social media reshaped education, enhancing access to resources.
```

**Iterative Token Reduction (V3):**
```
Social media revolutionized education.
```

## Project Structure

```
ai-text-compression-suite/
├── compress.py        # Contains all compression techniques
├── main.py            # Entry point to run & test compressions
├── config.py          # Model configuration (Gemini / AI model)
├── document.txt       # Sample input document
├── .env               # Example environment variables (API keys)
├── requirements.txt   # Dependencies list
└── README.txt         # Project documentation
```

## Compression Techniques

**Lexical Compression:** Rule-based removal of stopwords and redundant terms

**Semantic Compression:** AI-driven compression maintaining semantic meaning

**Task-Oriented Compression:** Context-aware compression for specific applications

**Map-Reduce Compression:** Scalable approach for large documents

**Latent Compression:** Deep semantic understanding and compression

**Iterative Token Reduction:** Multi-stage progressive compression

## Dependencies

- google-generativeai (Gemini SDK)
- python-dotenv

## Requirements

- Python 3.10+
- Google Gemini API key
- Internet connection
- Sample document (document.txt included)

## Use Cases

- Text summarization research
- NLP experimentation
- Knowledge distillation projects
- Storage-efficient AI applications
- Document compression workflows
- Academic research in text processing

## Notes

- Ideal for researchers and NLP enthusiasts
- Supports multiple compression strategies
- Preserves essential information while reducing size
- Configurable compression ratios
- Easy to extend with custom techniques

## Built with

- Python
- Google Gemini API
- Natural Language Processing techniques

