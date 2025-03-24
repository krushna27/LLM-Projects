# LLM-Projects
Project on text generation using the Hugging Face model facebook/opt-125m! and GPT-2 model Leveraging the powerful ultrachat_200k dataset.

Note:: Download the repo and used GPT2rebuild.py file only, opt125 model is just for practise purpose. 

Dataset - https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
Live code - https://gpttxtgen.streamlit.app/

Overview:
Developed and deployed a text generation application leveraging a fine-tuned GPT-2 model for generating domain-specific responses based on a custom dataset. The project focused on utilizing advanced NLP techniques, fine-tuning pre-trained LLMs, and building a user-friendly deployment interface.

Key Contributions:
Fine-Tuning GPT-2:

Fine-tuned the GPT-2 model on a custom conversational dataset (HuggingFace Ultrachat_200k).

Implemented advanced tokenization, padding, and hyperparameter tuning (learning rate: 2e-5, batch size: 16, epochs: 1) to optimize the model's performance on domain-specific queries.

Data Preprocessing:

Extracted and prepared text data from the dataset using NLP techniques such as tokenization, truncation, and max sequence length adjustments.

Mapped and processed dataset columns to train and evaluate the fine-tuned model effectively.

Streamlit Deployment:

Built an interactive web application using Streamlit to allow users to generate text based on specific prompts.

Enabled real-time user interaction with parameters like max length and temperature to adjust the creativity and precision of the output.

Incorporated robust error handling to manage out-of-scope prompts and guide users to ask dataset-relevant questions.

Customization and Output:

Designed the application to respond with meaningful outputs only to dataset-relevant queries, ensuring alignment with the fine-tuned model's scope.

Example: For queries related to London landmarks, the model generates accurate and coherent descriptions.

Deployment:

Successfully deployed the application on a local server using Streamlit for real-time demonstration.

Provided clear instructions for usage and ensured a seamless user experience.

Technologies & Tools:
Language Model: OpenAI GPT-2 (Fine-tuned using HuggingFace Transformers)
Frameworks: HuggingFace Transformers, PyTorch, Streamlit
Deployment Tools: Streamlit.



![ss](https://github.com/user-attachments/assets/ee3363dc-c474-4dc1-8931-9b3ed73eaf46)


