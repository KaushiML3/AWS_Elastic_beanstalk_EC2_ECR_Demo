# Deploying python applications in aws server

This repository contains the source code and deployment configuration for simple python app, a web-based platform for project management. The application is hosted on AWS, leveraging the power of cloud infrastructure for scalability, reliability, and performance.


## Features

- **AWS Deployment**: The application is deployed using AWS services, including EC2, S3, RDS, and others as applicable.
- **Scalability**: Built to scale with the use of [specific AWS features like Auto Scaling Groups, Elastic Load Balancer].
- **Security**: Implements secure access with IAM roles, security groups, and SSL/TLS encryption.
- **Automation**: Supports CI/CD pipelines with [mention the tool, e.g., AWS CodePipeline, GitHub Actions].


## Architecture

The application is deployed using the following AWS components:

    EC2 Instances: To host the backend application.
    Elastic Load Balancer: For load balancing across multiple instances.
    RDS (Relational Database Service): For database management.(Not include this repository)
    S3 (Simple Storage Service): For storing static files and application backups.
    CloudWatch: For monitoring and logging.

![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/1619870995631.png)



## AWS Deployment method

1. Elastic Beanstalk
2. EC2 
3. ECS


## Common steps

This step includes all common steps before doing deployment on all deployments (Elastic Beanstalk,EC2,ECS).

1. Create route53 web address
2. Create public VPC
3. Create security group for allow ssh and http/https
4. Create EC2 key pair
5. Iam role

### 1. Create route53 web address



### 2. Create public VPC

VPC (Virtual Private Cloud) is a service offered by AWS that allows you to create a logically isolated network within the AWS cloud. It gives you complete control over your virtual networking environment, including selecting your own IP address ranges, creating subnets, configuring route tables, and setting up network gateways.

![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(55).png)




### 3. Create security group for allow ssh and http/https

A Security Group in AWS is a virtual firewall that controls inbound and outbound traffic for your resources, such as EC2 instances, RDS databases, and other services. It acts as the first layer of defense for your resources by allowing or denying traffic based on defined rules.

Types of Rules in a Security Group
    - Inbound Rules:
        Control traffic that is allowed to reach your instance.
        Example:
            Allow SSH access: TCP, Port 22, Source: 0.0.0.0/0 (or specific IP range for security).

    - Outbound Rules:
        Control traffic that is allowed to leave your instance.
        Example:
            Allow all outbound traffic: Protocol: All, Destination: 0.0.0.0/0.


Web Server:
    Allow HTTP (port 80) and HTTPS (port 443) traffic from the internet (0.0.0.0/0).
    Allow SSH (port 22) access from a specific IP range (e.g., your office's IP).

Database Server:
    Deny all inbound traffic from the internet.
    Allow traffic from a specific web server's security group on port 3306 (for MySQL).

Private Backend Instances:
    Only allow traffic from the load balancer's security group.

![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(54).png)


1. Allow full SSH access for developers

- use your default or previous created vpc
![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(57).png)



2. Allow inbound internet access

- use your default or previous created vpc
![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(58).png)



### 4. Create EC2 key pair

An EC2 Key Pair in AWS is a set of security credentials used to securely connect to your Amazon EC2 instances. It consists of two parts:

    Public Key: Stored by AWS and associated with your EC2 instance.
    Private Key: Downloaded and stored securely on your local machine.

When you launch an EC2 instance, AWS uses the public key to encrypt the login credentials (e.g., a password). You use the private key to decrypt this information and securely log in to the instance.

![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(59).png)

### 5. Iam role

An AWS IAM Role is a tool within Amazon Web Services (AWS) Identity and Access Management (IAM) that allows entities (such as users, applications, or services) to assume temporary security credentials to interact with AWS resources. IAM roles are often used to delegate permissions without needing long-term credentials

- step 1:
    create EC2 role
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(63).png)

- step 2:
    add permission to "AWSElasticBeanstalkWebTier","AWSElasticBeanstalkWorkerTier","AWSElasticBeanstalkMulticontainerDocker" policy.

- step 3:
    Create Role name "EC2_instances_role"
     ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(64).png)







## 1. Elastic Beanstalk

**Amazon Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.**

step 1:
    Go to Amazon Elastic Beanstalk
    Create application with environment
    ![AWS Deployment Diagram]()

step 2:
    use default Existing service roles.
    add previouse created EC2 key pair.(Common steps 4)
    add previouse created EC2 instance profile.(Common steps 5)
     ![AWS Deployment Diagram]()


step 3:
    use default VPC or created vpc(Common steps 2)
     ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(65).png)

step 4:
    add the previouse created security group.(Common steps 3)
    use t3.micro or t2.mico
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(66).png)
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(67).png)
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(68).png)

step 5:
    set the helth reporting basic
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(69).png)

step 6:
    Create the environment.

finally :
    Go to domain.(you can see the host application)
    Need to change the application resource code. Click the upload and deploy. set the "aws_flask.zip","run_app.zip" or "run_main.zip" ,and deploy.
    
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(71).png)




   

**add the additional steps for CD**

step 1:
    Go to aws codepipeline
    create new pipelin and select build new templete
    ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(72).png)

step 2:
    Create pileline name. othors are default
     ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(73).png)

step 3:
    Source provider github.
     ![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(74).png)

step 4:
    Build provider skip
     
finally:
    Source and Deploy succuss . you can go to aws Elastic Beanstalk

## 2. EC2

![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(56).png)

step 1:
    create the EC2 instance
![AWS Deployment Diagram](https://github.com/KaushiML3/AWS_CD_test/blob/main/src_img/Screenshot%20(60).png)


step 2:
    connected the EC2 instance

step 3:

    sudo su #access root 
    yum 
