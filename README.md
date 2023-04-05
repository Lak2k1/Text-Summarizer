### Software And Tools Requirements

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

# Text Summarizer using Pegasus-CNN_DailyMail
This project is a text summarizer that utilizes the Pegasus-CNN_DailyMail model from Hugging Face's Transformers library. The model has been fine-tuned on the Samsum dataset to produce high-quality summaries of input texts.

## Features
- Automatic text summarization using abstractive methods
- Customizable level of detail in the generated summaries
- Support for multiple languages

## Requirements
- Python 3
- PyTorch
- Transformers
- Datasets

## Training
- The model used in this project was fine-tuned on the Samsum dataset using Google Colab. Due to the resource-intensive nature of the training process, fine-tuning on a normal laptop is not recommended. However, if you wish to train the model on your own dataset, you can do so by following these steps:

- Download and preprocess your dataset.
- Modify the existing model file to use your dataset and adjust any necessary hyperparameters.


## Conclusion
- Overall, this project demonstrates the effectiveness of transformer-based models for text summarization tasks. By fine-tuning the Pegasus-CNN_DailyMail model on the Samsum dataset, this text summarizer can produce high-quality summaries of input texts. While the training process may require specialized hardware or cloud-based services, the end result is a powerful tool for automatically summarizing large amounts of text.

![](https://github.com/Lak2k1/Text-Summarizer/blob/main/text-summary.gif)
