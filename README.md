\# ☁️ AWS Static Website Deployment Using Python + boto3



\## 1. Project Title



\*\*Automated Static Website Hosting and Deployment Using Python, boto3 and Amazon S3\*\*



\---



\## 2. Objective



The objective of this project is to automate the deployment of a static website to Amazon S3 using Python and the AWS SDK for Python (boto3).



The Python deployment script automatically:



\- Creates an Amazon S3 bucket

\- Configures static website hosting

\- Configures public access settings

\- Creates the required bucket policy

\- Uploads HTML, CSS and JavaScript files

\- Displays the S3 website URL



This reduces the need to manually configure S3 through the AWS Management Console.



\---



\## 3. Technologies Used



\- Python

\- boto3

\- Amazon S3

\- HTML

\- CSS

\- JavaScript

\- AWS CLI

\- Git

\- GitHub



\---



\## 4. AWS Services



\### Amazon S3



Amazon S3 is used to:



\- Store website files

\- Host the static website

\- Provide the website endpoint



\### IAM



AWS IAM is used to provide programmatic access through an IAM user.



\### AWS CLI



AWS CLI is used to configure AWS credentials and verify AWS access.



\---



\## 5. Architecture



```text

&#x20;                Developer

&#x20;                    |

&#x20;                    |

&#x20;                Python

&#x20;                deploy.py

&#x20;                    |

&#x20;                    | boto3

&#x20;                    ↓

&#x20;             AWS IAM Credentials

&#x20;                    |

&#x20;                    ↓

&#x20;             Amazon S3 Bucket

&#x20;                    |

&#x20;         +----------+----------+

&#x20;         |          |          |

&#x20;         ↓          ↓          ↓

&#x20;      HTML        CSS        JavaScript

&#x20;         |          |          |

&#x20;         +----------+----------+

&#x20;                    |

&#x20;                    ↓

&#x20;            S3 Static Website

&#x20;                    |

&#x20;                    ↓

&#x20;                  User

