# ☁️ Automated AWS S3 Static Website Deployment

A Python and **boto3-based automation project** that creates and configures an Amazon S3 bucket, enables static website hosting, applies the required access policy, and automatically uploads website files.

The project demonstrates how AWS infrastructure and application deployment tasks can be automated using Python instead of performing every configuration step manually through the AWS Management Console.

---

## 📌 Project Overview

This project automates the deployment of a static website on **Amazon S3** using the AWS SDK for Python (**boto3**).

The deployment script performs the major S3 configuration tasks automatically:

* Creates an S3 bucket
* Configures static website hosting
* Configures public access settings
* Creates a bucket policy
* Uploads website files
* Displays the deployed website URL

The project is designed as a practical demonstration of **AWS cloud automation, Python scripting, Amazon S3, IAM, and static website hosting**.

---

## 🎯 Objectives

The main objectives of this project are:

1. Automate Amazon S3 bucket creation using Python.
2. Configure S3 static website hosting programmatically.
3. Upload HTML, CSS, and JavaScript files automatically.
4. Configure the required bucket permissions.
5. Reduce manual AWS Console configuration.
6. Demonstrate the use of the AWS SDK (`boto3`).
7. Deploy a functional static website using AWS infrastructure.

---

## 🏗️ Architecture

```text
                    👨‍💻 Developer
                         |
                         |
                         ↓
                  Python Application
                     deploy.py
                         |
                         | boto3
                         ↓
                  AWS IAM Credentials
                         |
                         ↓
                   Amazon S3
                         |
              ┌──────────┼──────────┐
              ↓          ↓          ↓
            HTML        CSS        JavaScript
              |          |          |
              └──────────┼──────────┘
                         |
                         ↓
                S3 Static Website
                         |
                         ↓
                    🌐 End User
```

---

## 🛠️ Technologies Used

| Technology | Purpose                                 |
| ---------- | --------------------------------------- |
| Python     | Automation and deployment script        |
| boto3      | AWS SDK for Python                      |
| Amazon S3  | Static website hosting and file storage |
| IAM        | AWS authentication and permissions      |
| HTML       | Website structure                       |
| CSS        | Website styling                         |
| JavaScript | Client-side functionality               |
| AWS CLI    | AWS credential and access verification  |
| Git        | Version control                         |
| GitHub     | Source code repository                  |

---

## ☁️ AWS Services Used

### Amazon S3

Amazon S3 is the primary AWS service used in this project.

It is responsible for:

* Creating the storage bucket
* Hosting static website files
* Storing HTML, CSS, and JavaScript files
* Serving the website to users

### IAM

AWS IAM is used to provide the required permissions for programmatic access to AWS resources.

The Python application uses AWS credentials with appropriate permissions to interact with Amazon S3.

### AWS CLI

AWS CLI can be used to:

* Configure AWS credentials
* Verify AWS account access
* Test AWS connectivity
* Confirm that the required permissions are available

---

# 📂 Project Structure

```text
automated-s3-static-website/
│
├── website/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── aws-s3-bucket.png
│   ├── website.png
│   └── deployment.png
│
├── deploy.py
├── index.html
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact files inside the `website` and `screenshots` folders may vary depending on the final version of the project.

---

# ⚙️ How the Project Works

The deployment process follows these steps:

### Step 1 — Start the Python Deployment Script

The `deploy.py` program is executed by the developer.

```text
deploy.py
     ↓
Initialize boto3
```

---

### Step 2 — Create S3 Bucket

The script connects to Amazon S3 and creates the required bucket.

```text
Python
  ↓
boto3
  ↓
Amazon S3
  ↓
Create Bucket
```

---

### Step 3 — Configure Static Website Hosting

The script configures the bucket for static website hosting.

The website uses:

```text
index.html
```

as the main webpage.

---

### Step 4 — Configure Bucket Access

The deployment script configures the required S3 access settings and bucket policy so that the static website can be accessed through the S3 website endpoint.

---

### Step 5 — Upload Website Files

The website files are uploaded automatically.

Example:

```text
index.html
style.css
script.js
```

The script can determine the appropriate content type while uploading files.

---

### Step 6 — Display Website URL

After successful deployment, the script displays the S3 static website endpoint.

Example:

```text
Website deployed successfully!

Website URL:
http://<bucket-name>.s3-website-<region>.amazonaws.com
```

The exact URL depends on the AWS region and bucket configuration.

---

# 🚀 Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Yashodhan121/automated-s3-static-website.git
```

Move into the project directory:

```bash
cd automated-s3-static-website
```

---

## 2. Install Python Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project uses:

```text
boto3
```

---

## 3. Configure AWS Credentials

Configure AWS credentials using the AWS CLI:

```bash
aws configure
```

Provide:

```text
AWS Access Key ID
AWS Secret Access Key
Default region name
Default output format
```

Example region used for this project:

```text
ap-south-1
```

> Never upload AWS access keys or secret keys to GitHub.

---

# ▶️ Run the Deployment

Execute:

```bash
python deploy.py
```

The script will perform the required deployment operations automatically.

Expected flow:

```text
Starting deployment...
        ↓
Creating S3 bucket...
        ↓
Configuring website hosting...
        ↓
Configuring bucket policy...
        ↓
Uploading website files...
        ↓
Deployment completed
        ↓
Website URL displayed
```

---

# 🌐 Website Deployment

After successful execution, the website is hosted using the Amazon S3 static website hosting feature.

The deployment architecture is:

```text
             Python deploy.py
                    |
                  boto3
                    |
                    ↓
              Amazon S3 Bucket
                    |
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       index.html  CSS       JS
          |
          ↓
     Static Website
          |
          ↓
        Browser
```

---

# 📸 Project Screenshots

The `screenshots/` directory contains screenshots demonstrating the project and AWS deployment.

Recommended screenshots include:

### 1. S3 Bucket

Shows the created S3 bucket in the AWS Management Console.

### 2. Website Files

Shows the uploaded HTML/CSS/JavaScript files inside the S3 bucket.

### 3. Static Website Configuration

Shows that static website hosting has been configured.

### 4. Bucket Policy

Shows the configured S3 bucket policy.

### 5. Live Website

Shows the successfully deployed website in a browser.

### 6. Python Deployment Output

Shows the successful execution of `deploy.py` and the generated website endpoint.

---

# 🔐 Security Considerations

AWS credentials must **never** be committed to GitHub.

Do not include:

```text
AWS Access Key
AWS Secret Access Key
.env
credentials
private keys
```

Use `.gitignore` to prevent sensitive files from being committed.

For production environments, prefer:

* IAM roles
* Least-privilege IAM policies
* Temporary credentials
* CloudFront + HTTPS
* Private S3 buckets where appropriate

---

# 📊 Project Features

| Feature                     | Status |
| --------------------------- | ------ |
| Python automation           | ✅      |
| boto3 integration           | ✅      |
| S3 bucket creation          | ✅      |
| Static website hosting      | ✅      |
| Website file upload         | ✅      |
| Bucket policy configuration | ✅      |
| AWS CLI integration         | ✅      |
| GitHub repository           | ✅      |
| Deployment URL              | ✅      |
| Screenshots/documentation   | ✅      |

---

# 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Amazon S3
* Static website hosting
* AWS IAM
* AWS CLI
* Python automation
* boto3
* AWS SDK usage
* Cloud deployment
* Bucket policies
* Object storage
* Git and GitHub
* Infrastructure automation concepts

---

# 💡 Advantages

### Manual Deployment

```text
AWS Console
    ↓
Create Bucket
    ↓
Configure Hosting
    ↓
Configure Permissions
    ↓
Upload Files
    ↓
Get Website URL
```

### Automated Deployment

```text
Python deploy.py
       ↓
     boto3
       ↓
Amazon S3
       ↓
Complete Deployment
```

Automation makes the deployment process faster, repeatable, and less dependent on manual configuration.

---

# 🔮 Future Enhancements

The project can be extended with additional AWS services and automation features.

Possible improvements include:

* Amazon CloudFront integration
* HTTPS using AWS Certificate Manager
* Custom domain using Route 53
* CI/CD using GitHub Actions
* Automatic deployment whenever code is pushed to GitHub
* S3 versioning
* CloudWatch monitoring
* Automated rollback
* Infrastructure as Code using AWS CloudFormation or Terraform
* Separate development and production environments

---

# 🧪 Testing

The deployment can be verified by checking:

### AWS S3

Confirm that the bucket exists.

### Bucket Objects

Confirm that the website files have been uploaded.

### Website Endpoint

Open the generated S3 website URL in a browser.

### Website Functionality

Verify:

* HTML loads correctly
* CSS is applied
* JavaScript functions correctly
* Website assets are accessible

---

# 📌 Project Repository

**GitHub Repository:**

https://github.com/Yashodhan121/automated-s3-static-website

---

# 👨‍💻 Author

**Yashodhan Kolhe**

GitHub:

https://github.com/Yashodhan121

---

# 📜 License

This project is created for **educational and demonstration purposes**.

You may modify and extend the project for learning and academic use.
