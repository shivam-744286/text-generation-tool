# text-generation-tool

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SHIVAM KUMAR

*Intern id*: CT04DN1277

*DOMAIN*: Artificial Intelligence

*DURATION*: 4 weeks

*MENTOR*: NEELA SANTOSH

This project is done using Visual Studio Code (VS Code). It's available for Windows, macOS, and Linux, and also has a web version. VS Code is a source code editor that combines developer tooling, a frictionless edit-build-debug cycle, and a rich ecosystem of extension.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/3196c73f-38f6-43ad-8c42-10211e1bcf18)

![Image](https://github.com/user-attachments/assets/d4b17e91-11f1-4e57-baba-d4918ceb39d3)

This project is a Python-based implementation that uses GPT-2, a powerful AI model developed by OpenAI, to generate human-like text based on a user-provided prompt.

Using the Hugging Face Transformers library and PyTorch, the script loads the GPT-2 model and tokenizer, allows user input, and generates natural language responses or paragraphs.

How It Works

Libraries Used:
->transformers – for loading GPT-2 and its tokenizer.
->torch – to run the model on CPU or GPU using PyTorch.

Model Loading:

->It loads the GPT-2 tokenizer (which breaks text into tokens) and GPT-2 model (which generates the text).
->The pad token is manually set to avoid warnings/errors.

Device Detection:
->Automatically detects if your system has a GPU (CUDA) or CPU, and loads the model accordingly.

User Input:

The user is asked to enter:
->A prompt (starting line or idea for the AI).
->A maximum word limit (how long the response should be).

Text Generation:

The model encodes the prompt and generates new text based on it.

It uses techniques like:

->Top-k sampling – picks from top k likely words.
->Top-p sampling – filters based on probability threshold.
->Temperature – controls randomness (0.7 = balanced).
->No repetition – prevents repeated phrases.

Output:

The generated text is printed to the screen after removing special tokens.
