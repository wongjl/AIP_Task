This repository contains a simple app on Visual QA on uploaded documents in image format.

## Setup
**Software Pre-requisites**
1) Docker

**Setup Steps**
1) Git clone/download the repository into a folder such as 'AIP_TASK'.
2) Run *Terminal* and change the working directory to AIP_TASK such that the working directory contains the *docker-compse.yaml* file.
3) Run the following command to setup the docker containers using Docker Compose. There will be 2 containers 'frontend' and 'backend' after the setup is completed.
```
docker compose up -d
```

**Usage Information**
1) Go to the following URL with any web browser.
```
http://localhost:8077/predict/
```
You should be directed to a page similar to the below screenshot.
![interface](https://github.com/wongjl/AIP_Task/blob/main/images/interface.png)

2) Fill in the URL link and question textbox and click on 'Run'.

## Model Information
**Inputs**
The frontend interface will require 2 inputs.
1) URL link to the uploaded image
2) Question to be answered from the image

**Ouputs**
1) Predicted answer from the image that best answer the question, with the correesponding score

## Examples
**Example 1**

Inputs:
```
Image URL: https://www.accountingcoach.com/wp-content/uploads/2013/10/income-statement-example@2x.png
Question: What are the 2020 net sales?
```

![example1](https://github.com/wongjl/AIP_Task/blob/main/images/example1.png)

**Example 2**

Inputs:
```
Image URL: https://templates.invoicehome.com/invoice-template-us-neat-750px.png
Question: What is the invoice number?
```

![example2](https://github.com/wongjl/AIP_Task/blob/main/images/example2.png)

**Example 3**

Inputs:
```
Image URL: https://docular.net/previews/docx/5506-001.png
Question: What role is the appointed person?
```

![example3](https://github.com/wongjl/AIP_Task/blob/main/images/example3.png)

**Example 4 (Attempt on non-answerable question)**

Inputs:
```
Image URL: https://docular.net/previews/docx/5506-001.png
Question: How much do I pay for security? 
```

![example4](https://github.com/wongjl/AIP_Task/blob/main/images/example4.png)
