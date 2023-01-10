---
jupyter:
  colab:
    collapsed_sections:
    - oTvNzYU3qDf4
    - Bh0x1O9lVIMf
    - wXx0MoA1m0K8
    - LenrMJf2DkI0
    - JhbSo-mJRJ5c
    - \_CYAZ1KL0p1u
    - CQ6WOe7BWhm1
  kernelspec:
    display_name: Python 3
    name: python3
  language_info:
    name: python
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="F4RJsDZXp0-n"}
# AWS CLOUD PRACTITIONER CERTIFICATION
:::

::: {.cell .markdown id="oTvNzYU3qDf4"}
## 1. WHAT IS CLOUD COMPUTING? {#1-what-is-cloud-computing}
:::

::: {.cell .markdown id="8ESmSpVVqMhF"}
**SERVER**

-   CPU (Compute)
-   RAM (Memory)
-   Data (Storage)
-   Database (Store data in structured way)
-   Network (Cables, routers and servers connected with each other)
-   Router (A networking device that forwards data packets between
    computer networks. They know where to send your packets on the
    internet)
-   Switch (Takes a packet and send it to the correct server/client on
    your network)

`<br>`{=html}

**PROBLEMS WITH TRADITIONAL IT APPROACH**

-   Pay for the rent for the data center
-   Pay for power supply, cooling, maintenance
-   Adding and replacing hardware takes time
-   Scaling is limited
-   Hire 24/7 team to monitor the infrastructure
-   How to deal with disasters? (earthquake, power shutdown, fire)

`<br>`{=html}

**CLOUD COMPUTING**

-   On demand delivery of compute power, database storage, applications,
    IT services
-   Pay-as-you-go pricing\
-   Provision exactly the right type and size of computing resources you
    need
-   Access many resources as you need, almost instantly
-   Simply way to access servers, storage, databases abd set of
    application services

`<br>`{=html}

**DEPLOYMENT MODELS OF THE CLOUD**

-   *PRIVATE CLOUD*:
    -   Cloud used by single organization, not exposed to the public
    -   Complete control
    -   Security for sensitive application
    -   Meet specific business needs
-   *PUBLIC CLOUD*:
    -   Cloud resources owned and operated by a third-part cloud service
        provider delivered on the internet
    -   6 advantages of cloud computing\
-   *HYBRID CLOUD*:
    -   Keep some servers on premises and extend some capabilities to
        the cloud
    -   Control over sensitive assets in your private infrastructure
    -   Flexibility and cost effectiveness of the public cloud

`<br>`{=html}

**THE 5 CHARACTERISTICS OF CLOUD COMPUTING**

-   *On demand self service*: Users can provision resources and use them
    without human interaction from the service provider
-   *Broad network access*: Resources available over the network
-   *Multi-tenancy and resource pooling*: Multiple customers can share
    the same infrastructure with security and privacy and they are
    serviced from the same physical resources
-   *Rapid elasticity and scalability*: Automatically and quickly
    acquire and dispose resources when needed and easily scale based on
    demand
-   *Measured service*: Usage is measured, users pay correctly for what
    they have used

`<br>`{=html}

**THE 6 ADVANTAGES OF CLOUD COMPUTING**

-   *Trade capital expense (CAPEX) for operational enpense (OPEX)*: Pay
    on demand, don\'t own hardware and reduce total cost of ownership
-   *Benefit from massive economies of scale*: Prices are reduced as AWS
    is more efficient due to large scale
-   *Stop guessing capacity*: Scale based on actual measured usage
-   *Increase speed and agility*
-   *Stop spending money running and maintaining data centers*
-   *Go global in minutes*

`<br>`{=html}

**PROBLEMS SOLVED BY THE CLOUD**

-   *Flexibility*: Change resource types when needed
-   *Cost-Effectiveness*: Pay as you go for what you use
-   *Scalability*: Accomodate larger loads by making hardware stronger
    or adding additional nodes
-   *Elasticity*: Ability to scale out and scale-in when needed
-   *High available and fault tolerance*: Build across data centers
-   *Agility*: Rapidly develop, test and launch software application

`<br>`{=html}

**TYPES OF CLOUD COMPUTING**

-   *Infrastructure as a Service (EC2)*:
    -   Provide bulding blocks for cloud IT
    -   Provides networking, computers, data storage space
    -   Highest level of flexibility
    -   Easy parallel with traditional on-premises IT
-   *Platform as a Service (Elastic Beanstalk)*:
    -   Removes the need for your organization to manage the underlying
        infrastructure
    -   Focus on the deployment and management of your applications
-   *Software as a Service (Rekognition, Google Maps)*:
    -   Completed product that is run and managed by the service
        provider

`<br>`{=html}

**PRICING OF THE CLOUD**

-   *Compute*: Pay for compute time
-   *Storage*: Pay for data stored in the Cloud
-   *Data Transfer OUT*: Data transfer IN is free

`<br>`{=html}

**AWS GLOBAL INFRASTRUCTURE**

-   *AWS REGION*
    -   Region all around the world (us-east-1, eu-west-3)
    -   Cluster of data centers
    -   Most AWS services are region-scoped (*IAM*, *Route 53*, *WAF*:
        examples of global services)
    -   Choose the region according to the data governance and legal
        requirements
    -   Proximity to customers to reduce latency
    -   Available services within a region
    -   Pricing which can vary from a region to another

`<br>`{=html}

-   *AWS AVAILABILITY ZONES*
    -   Each region has many availability zones (min 2, max 6,
        usually 3)
    -   Each AZ is one or more discrete ddata ccenters with redundant
        power
    -   They\'re isolated from disasters
    -   They\'re connected with high bandwidth, ultra-low latency

`<br>`{=html}

-   *AWS POINT OF PRESENCE (EDGE LOCATIONS)*
    -   Amazon has 216 points of presencein 84 cities and 42 countries
    -   Content is delivered to end user with lower latency
:::

::: {.cell .markdown id="Bh0x1O9lVIMf"}
## 2. IAM SECTION {#2-iam-section}
:::

::: {.cell .markdown id="c6tLgrePVUa5"}
**IAM: Identity and Access Management**

-   *USERS*: They are people within your organization and can be
    grouped. There is a root account created by default and it
    shouldn\'t be used or shared.
-   *GROUPS*: They only contains users, not other groups and users
    don\'t have to belong to a group and can belong to multiple groups.
-   *POLICIES*: Users or groups can be assigned JSON documents called
    policies. These policies define the permission of the users. In AWS
    you apply the least privilege principle, don\'t give more permission
    than a user needs.
-   *SECURITY*: Password policy + MFA (Multi Factor Authentication).
-   *AWS CLI*: Manage your AWS services by the command line. Direct
    access to the public APIs of AWS services. Alternative to AWS
    Management Console.
-   *AWS SDK*: Manage your AWS services using a programming language
    (Software Development Kit) with language specific APIs.
-   *Access Keys*: To access AWS using the CLI or SDK. They are
    generated through the AWS Management Console and they are like a
    password.
-   *IAM ROLES*: They are just like a user but they are intended to be
    used not by physical people but instead they will be used by AWS
    services that need to perform actions on your behalf (EC2, Lambda).
-   *IAM SECURITY TOOLS*: IAM Credentials Report that lists all your
    account\'s users and the status of the various credentials and IAM
    Access Advisor which shows the service permissions granted to a
    userand when those services were last accessed.
:::

::: {.cell .markdown id="wXx0MoA1m0K8"}
## 3. EC2 SECTION {#3-ec2-section}
:::

::: {.cell .markdown id="6Uy6I3U0m60W"}
**EC2: Elastic Compute Cloud**

`<br>`{=html}

**EC2**

It mainly consists in the capability of:

-   Renting virtual machines (EC2)
-   Storing data on virtual drives (EBS)
-   Distributing load across machines (ELB)
-   Scaling the services using an auto-scaling group (ASG)

**EC2 Configuration**

-   Operating System: Linux, Windows or MacOS
-   How much compute power & cores (CPU)
-   How much random-access memory (RAM)
-   How much storage space:
    -   Network attached (EBS & EFS)
    -   Hardware (EC2 Instance Store)
-   Network Card: speed of the card, Public IP address
-   Bootstrap script (configure at first launch): EC2 User Data

**EC2 Instance Types**

-   m5.2xlarge (e.g.):
    -   *m*: Instance class
    -   *5*: Generation (AWS improves over time)
    -   *2xlarge*: Size within the instance class
-   *General Purpose*: Great for a diversity of workloads such as web
    servers or code repositories. Balance between compute, memory and
    networking.
-   *Compute Optimized*: Great for compute intensive tasks that require
    high performance processors as batch processing workloads,
    scientific model and machine learning or gaming servers.
-   *Memory Optimized*: Fast performance for workloads that process
    large data sets in memory as high perf relational/non-relational
    databases or distributed web scale cache stores.
-   *Storage Optimized*: Great for storage intensive tasks that require
    high, sequential read and write access to large data sets on local
    storage as cache for in memory databases (Redis).

**EC2 Security Groups**

Security groups are acting as a firewall on EC2 instances, they control
how traffic is allowed into or out our EC\" instances. Security groups
only contain allow rules and can reference by IP or by security group.
They regulate:

-   Access to ports
-   Authorized IP ranges - IPv4 and IPv6
-   Control of inbound network (from other to instance, blocked by
    default)
-   Control of outbound network (from instance to other, authorized by
    default)

**EC2 User Data**

It\'s possible to bootstrap (launching commands when a machine start)
ourinstances using an EC2 User Data script. That script is only run once
at the instance first start and it run with the root user. It\'s used to
automate boot tasks such as:

-   Installing updates
-   Installing software
-   Downloading common files from internet
-   Anything you can think of

**SSH**

It allows you to control a remote machine, all using the command line.
We can configure all the parameters using the free tool \"Putty\".

**Purchasing Options**

-   *EC2 On-Demand Instances*: Linux/Windows billing per seconds after
    the first minute, otherwise billing per hour. Has the highest cost
    but no upfront payment. No long-term commitment and recommended for
    short term and un-interrupted workloads.
-   *EC2 Reserved Instances*: Uo to 72% discount (compared to
    on-demand). You reserve a specific instance attributes (instance
    type, region, tenancy, OS) with a reservation period of 1 or 3 years
    with different payment options:
    -   No Upfront (+)
    -   Partial Upfront (++)
    -   All Upfront (+++) You can reserve an instance scope, regional or
        zonal and it\'s recommended for steady-state usage applications
        (db) and you can buy and sell in the Reserved Instance
        Marketplace.
-   *EC2 Convertible Reserved Instance*: Can change EC2 instance type,
    instance family, OS, scope and tenancy and you can get up to 66% of
    discount.
-   *EC2 Saving Plans*: Get a discount based on long-term usage and
    commit to a certain type of usage (e.g. \$10/hour for 1/3 years),
    usage beyond EC\" Saving Plans is billed at the on-demand rate.
    It\'s flexible across instance size, OS and tenancy.
-   *EC2 Spot Instances*: Instances that you can lose at any point of
    time if your max price is less than the current spot price. It\'s
    the most cost-efficient instances in AWS and you can get a discount
    of up to 90% compared to on-demand. It\'s useful for workload that
    are resilient to failure as batch jobs, data analysis or image
    processing and it\'s not suitable for critical jobs or databases.
-   *EC2 Dedicated Hosts*: A physical server with EC2 instance capacity
    fully dedicated to your use, that\'s the most expensive option.
    Purchasing option:
    -   On-demand: pay per second for active Dedicated Host
    -   Reserved: 1 or 3 years (No/Partial/All Upfront)
-   *EC2 Dedicated Instances*: Instance run on hardware that\'s
    decicated to you, you may share hardware with other instances in
    same account and there is no control over instance placement (can
    move hardware after stop/start).\
-   *EC2 Capacity Reservations*: Reserve on-demand instances capacity in
    a specific AZ for any duration. No time commitment or billing
    discount. You are charged at on-demand rate whether you run
    instances or not. Suitable for short term, uninterrupted workloads
    that needs to be in a specific AZ.

**Best Purchasing Option**

-   *On-Demand*: Coming and staying in resort whenever we like, we pay
    the full price
-   *Reserved*: Like planning ahead and if we plan to stay for a long
    time, we may get a good discount.
-   *Saving Plans*: Pay a certain amount per hour for certain period and
    stay in any room type (e.g. King, Suite, Sea View, etc\...)
-   *Spot Instances*: The hotel allows people to bid for the empty rooms
    and the highest bidder keeps the rooms. You can get kicked out at
    any time.
-   *Dedicated Host*: We book an entire building of the resort.
-   *Capacity Reservations*: You book a room for a period with full
    price even you don\'t stay in it.
:::

::: {.cell .markdown id="LenrMJf2DkI0"}
## 4. EC2 INSTANCE STORAGE SECTION {#4-ec2-instance-storage-section}
:::

::: {.cell .markdown id="uM_sQWFjDo8I"}
**EBS VOLUME: Elastic Block Store**

-   What is an EBS?
    -   It\'s a network drive you can attach to your instances while
        they run
    -   It allows your instances to persist data, even after termination
    -   They can only be mounted to one instance at a time
    -   They are bound to a specific availability zone: to move a volume
        across, you first need to snapshot it
    -   Free tier = 30GB of storage (you can increase the capacity of
        the drive over time)
    -   Analogy: Think of them as a \"Network USB stick\" (not a
        physical drive)
-   EBS Snapshots
    -   *Snapshot* = Backup of your EBS volume at a point in time
    -   Not necessary to detach volume to do snapshot but recommended
    -   Can copy snapshots across AZ or Region
    -   *EBS Snapshot Archive*: move a snapshot to an \"archive tier\"
        that is 75% cheaper but it takes within 24 to 72 hours for
        restoring the archive
    -   You can setup rules to retain deleted snapshots so you can
        recover them after an accidental deletion (you can specify
        retention from 1 day to 1 year)

**AMI: Amazon Machine Image**

-   Ready to use EC2 instances with our customization (own software,
    configuration, operating system, monitoring)
-   AMI are built for a specific region ( and can be copied across
    regions)
-   You can launch EC2 instances from:
    -   Public AMI: AWS provided
    -   Your own AMI: you make and mantain them yourself
    -   AWS Marketplace AMI: AMI someone else made
-   *AMI Process*:
    -   Start an EC2 instance and customize it
    -   Stop the instance
    -   Build an AMI - this will also create an EBS Snapshot
    -   Launch instances from other AMIs

**EC2 Image Builder**

-   Used to automate the creation of Virtual Machines or container
    images
-   Automate creation, mantain, validate and test of EC2 AMIs
-   Can be run on a schedule
-   Free service (only pay for the underlying resources)

**EC2 Instance Store**

-   EBS volumes are network drives with good but limited performance
-   If you need a high performance hardware disk, use *EC2 Instance
    Store*
-   Better I/O performance
-   EC2 Instance Store lose their storage if they\'re stopped
-   Risk of data loss if hardware fails
-   Good for buffer/cache/scratch data/temporary content

**EFS: Elastic File System**

-   Managed NFS (network file system) that can be mounted on 100s of EC2
-   EFS works with Linux EC2 insyances in multi-AZ
-   Highly available, scalable, expensive, pay per use

**EFS-IA: EFS Infrequent Access**

-   Storage class that is cost-optimized for files not accessed every
    day
-   Up to 92% lower cost compared to EFS standard
-   EFS will automatically move your files to EFS-IA based on last time
    they were accessed

**Amazon FSx**

Launch 3rd party high-performance file system on AWS

-   *Amazon FSx for Windows*
    -   A fully managed, highly reliable and scalable Windows native
        shared file system
    -   Build on Windows File Server
    -   Supports SMB protocol & windows NTFS
    -   Integrated with Microsoft Active Directory
-   *Amazon FSx for Lustre*
    -   A fully managed, high-performance, scalable file storage for HPC
        (High Performance Computing)
    -   The name \"Lustre\" derive from \"Linux\" and \"cluster\"
    -   Machine Learning, Analytics, Video Processing, Financial
        Modeling\...
    -   Scales up to 100s GB/s, sub-ms latencies
:::

::: {.cell .markdown id="JhbSo-mJRJ5c"}
## 5. ELASTIC LOAD BALANCING & AUTO SCALING GROUPS SECTION {#5-elastic-load-balancing--auto-scaling-groups-section}
:::

::: {.cell .markdown id="dCdog33MRUIL"}
**Scalability vs High Availability**

-   *Scalability*
    -   It means an application/system can handle greater loads by
        adapting
    -   It\'s linked but different to High Availability
    -   Vertical Scalability
        -   It means increase the size of the instance
        -   It is very common for non distributed systems, such as
            database
        -   There\'s usually a limit to how much you can vertically
            scale (hardware limit)
    -   Horizontal Scalability
        -   It means increase the number of instances/systems for your
            application
        -   It implies distributed systems
        -   This is very common for web applications/modern applications
        -   It\'s easy to horizontally scale thanks the cloud offerings
            such as Amazon EC2
-   *High Availability*
    -   It goes hand in hand with horizontal scaling
    -   It means running your application in at least 2 AZs
    -   The goal of high availability is to survive a data center loss
        (disaster)

**Scalability vs Elasticity vs Agility**

-   *Scalability*: ability to accomodate a larger load by making the
    hardware stronger (scale up) or by adding nodes (scale out)
-   *Elasticity*: once a system is scalable, elasticity means that there
    will be some auto-scaling so that the system can scale based on the
    load (cloud friendly)
-   *Agility*: (distractor) new IT resources are only a click away,
    which means that you reduce the time to make those resources
    available to your developers

**ELB: Elastic Load Balancer**

-   Distribute traffic across backend EC2 instances, can be multi AZ
-   Expose a single point of access (DNS) to your application
-   Do regular health checks to your instances
-   It\'s a managed load balancer: AWS guarantees that it will be
    working, takes care of upgrades and maintenance and provides only a
    few config knobs
-   Kind of load balancers offered by AWS:
    -   Application Load Balancer: HTTP/HTTPS (Layer 7)
    -   Network Load Balancer: ultra high-perf, TCP (Layer 4)
    -   Classic Load Balancer: slowly retiring (Layer 4 & 7)

**ASG: Auto Scaling Groups**

-   Implement Elasticity for your application, accross multiple AZ
-   Scale EC2 instances based on the demand on your system and replace
    unhealthy
-   Integrated with the ELB
-   Scaling strategies:
    -   Manual scaling: update size manually
    -   Simple/Step Scaling: when a CloudWatch alarm is triggered then
        do something\
    -   Target Tracking Scaling: e.g. I want avg ASG CPU to stay at
        around 40%
    -   Scheduled Scaling: anticipate scaling
    -   Predictive Scaling: ML to predict future traffic ahead of time
:::

::: {.cell .markdown id="_CYAZ1KL0p1u"}
## 6. AMAZON S3 SECTION {#6-amazon-s3-section}
:::

::: {.cell .markdown id="ibeqmP9a0xJu"}
*Amazon S3* is one of the main building blocks of AWS, it\'s advertised
as \"infinitely scaling\" storage. It has a lot of use cases as backup
and storage, disaster recovery, archive, application hosting, big data
analytics, software delivery and static website.

**Buckets vs Objects**

-   Buckets:
    -   Amazon S3 allows people to store objects (files) in \"buckets\"
        (directories)
    -   They must have a globally unique name
    -   They are at the region level
    -   S3 looks like a global service but buckets are created in a
        region
    -   There is a naming convention (no uppercase/underscore, 3-63
        chars long, start with lowercase or number, etc\...)
-   Objects:
    -   Object (files) have a key which is a full path (prefix + object
        name) e.g. s3://my-bucket/my_file.txt
    -   There is no concept of directories within buckets
    -   Max size is 5000GB and if uploading more than 5GB must use multi
        part upload
    -   Tags: useful for security/lifecycle
    -   Version ID: if versioning is enabled

**S3 Security**

-   User Based:
    -   IAM Policies: which API calls should be allowed for a specific
        user from IAM
-   Resource-Based:
    -   Bucket Policies: bucket wide rules from the S3 console - allow
        cross account
    -   Object Access Control List: finer grain
    -   Bucket Access Control List: less common
-   Note: an IAM principal can access an S3 if
    -   The user IAM permission allow it or the resource policy allows
        it
    -   And there is no explicit deny\
-   Policies:
    -   JSON based policies
        -   Resources: buckets and objects
        -   Effect: Allow/Deny
        -   Actions: Set of API to allow or deny
        -   Principal: The account or user to apply the policy to
    -   S3 bucket for policy:
        -   Grant public access to the bucket
        -   Force objects to be encrypted at upload

**S3 Websites**

-   S3 can host a static websites and have them accessible on the
    internet
-   The website URL depend on the bucket name and region\
-   403 forbidden error \--\> make sure the bucket policy allows public
    reads

**S3 Versioning**

-   You can version files in Amazon S3
-   It\'s enabled at the bucket level
-   It\'s best practice to protect against unintended deletes and easy
    roll back to previous version

**S3 Replication**

-   Must enable versioning in source and destination buckets
-   Cross-Region Replication (CRR): lowerlatency access,replication
    across accounts
-   Same-Region Replication (SRR): log aggregation, live replication
    between production and test accounts

**S3 Storage Classes**

-   *S3 Standard - General Purpose*
    -   99.99% availability
    -   Used for frequently accessed data
    -   Low latency
    -   Use case: big data analytics, mobile and game applications
-   *S3 Standard - Infrequent Access (IA)*
    -   For data less accessed, but requires rapid access when needed
    -   Lower cost than S3 standard
    -   99.9% availability
    -   Use cases: disaster recovery and backups
-   *S3 One-Zone - Infrequent Access*
    -   High durability (99.999999%) in a single AZ. Data lost if AZ is
        destroyed
    -   99.5% availability
    -   Use cases: storing secondary backup copiesof on-premises data
-   *S3 Glacier Instant Retrieval*
    -   Low cost object storage for archiving/backup
    -   Milliseconds retrieval
    -   Minimum storage duration of 90 days
-   *S3 Glacier Flexible Retrieval*
    -   Expedited (1-5 minutes), Standard (3-5 hours), Bulk (5-12 hours)
    -   Minimum storage duration of 90 days
-   *S3 Glacier Deep Archive*
    -   Standard (12 hours), Bulk (48 hours)
    -   Minimum storage duration of 180 days
-   S3 Intelligent Tiering\*
    -   Small monthly monitoring and auto tiering fee
    -   Moves objects automatically between Access Tiers based on usage

**AWS Snow Family**

Highly-secure, portable devices to collect and process data at the edge,
and migrate data into and out of AWS. Offline devices to perform data
migrations

-   Data Migration:
    -   AWS Snowball Edge
        -   Physical data transport solution, move TBs or PBs of data in
            or out of AWS
        -   Altenative to moving data over the network
        -   Pay per data transfer job
        -   Types:
            -   Snowball Edge Storage Optimized: 80 TB of HDD capacity
                for block volume
            -   Snowball Edge Compute Optimized: 42 TB of HDD capacity
                for block volume
        -   Use cases: large data cloud migrations, disaster recovery\
    -   AWS Snowcone
        -   Small (2kg), portable computing, secure, withstands harsh
            environments\
        -   Used for edge computing, storage (8 TBs) and data transfer
        -   Use Snowcone when Snowball does not fit (space-constrained)
        -   Must provide your own battery
    -   AWS Snowmobile
        -   Transfer exabytes of data (1 EB = 1K PBs = 1M TBs)
        -   Each snowmobile has 100 PB of capacity
        -   High security: temperature controlled, GPS, 24/7 video
            surveillance
        -   Better than Snowball if you transfer more than 10 PB
-   Edge Computing:
    -   Process data while it\'s being created on an edge location
        (track, ship, etc\...)
    -   These location may have no internet access or no easy access to
        computing power
    -   We setup a Snowball Edge/Snowcone device to do edge computing
    -   Use cases: Preprocess data, ML at the edge, transcoding media
        streams
    -   Types:
        -   Snowcone: 2 CPUs, 4GB of memory
        -   Snowball Edge - Compute Optimized: 52 CPUs, 208GB of RAM,
            optional GPU
        -   Snowball Edge - Storage Optimized: 40 CPUs, 80GB of RAM,
            object storage clustering available

**AWS OpsHub**

-   Historically to use Snow Family devices, you needed a CLI
-   Today you can use OpsHub, a software you install on your computer,
    to manage your Snow Family devices

**AWS Storage Gateway**

-   Bridge between on-premise data and cloud data in S3
-   Hybrid storage service to allow on-premises to seamlessly use the
    AWS Cloud
-   Use cases: disaster recovery, backup & restore, tiered storage
:::

::: {.cell .markdown id="CQ6WOe7BWhm1"}
## 7. DATABASES SECTION {#7-databases-section}
:::

::: {.cell .markdown id="M9FBcZqsWmdD"}
Storing data on disk (EFS, EBS, EC2 Instance Store, S3) can have its
limits. Sometimes you want to store data in a database to structure the
data and build indexes to efficiently query/search through the data

**Relational Databases**

-   AWS RDS (Relational Database Service)
    -   It\'s a managed DB service for DB use SQL asa query language
    -   It allows you to create databases in the cloud that are managed
        by AWS
        -   Postgres
        -   MySQL
        -   MariaDB
        -   Microsoft SQL Server
        -   AWS Aurora
    -   Automatic provisioning and OS patching
    -   Continuous backups and restore to specific timestamp
    -   Multi AZ for DR (disaster recovery)
    -   Scaling capability (vert & horiz)
-   AWS Aurora
    -   Not open sourced
    -   PostgreSQL and MySQL are both supported as Aurora DB
    -   Aurora is AWS cloud optimized
    -   Aurora storage automatically grows up to 64GB
    -   It costs more than RDS (20% more) but it\'s more efficient
    -   Not in the free tier

**ElastiCache**

-   Same as RDS but for Redis or Memcached
-   Caches are in-memory databases with high performance and low latency
-   Helps reduce load off databases for read intensive workloads

**DynamoDB**

-   Fully managed highly available with replication across 3 AZ
-   NoSQL database
-   Scales to massive db, distributed serverless db
-   Millions of requests per seconds, trillions of rows, 100s TB of
    storage
-   Single digit milliseconds latency
-   Integrated with IAM
-   Low cost and auto scaling
-   *DynamoDB Accelerator (DAX)*
    -   Fully managed in memory cache for DynamoDB
    -   10x performance improvement
    -   Secure, highly scalable and available
    -   It\'s only used for and is integrated with DynamoDB

**Redshift**

-   It\'s based on PostgreSQL but it\'s not for OLTP (Online Transaction
    Processing)
-   It\'s OLAP (Online Analytical Processing)
-   Load data every hour (not seconds)\
-   10x better performance than other warehouses
-   Columnar storage of data (instead of rows)
-   Has SQL interface
-   BI (business intelligence) tools such as AWS Quicksight or Tableau
    integrate with it

**Amazon EMR (Elastic MapReduce)**

-   EMR helps creating Hadoop clusters (Big Data) to analyze and process
    vast amount of data
-   The cluster can be made of hundreds of EC2 instances
-   Also supports Apache Spark, HBase, Presto, etc\...
-   EMR takes care of all the provisioning and configuration
-   Use cases: data processing, ML, web indexing, big data, etc\...

**Amazon Athena**

-   Serverless query service to analyze data stored in Amazon S3
-   Uses standard SQL language to query the files
-   Supports CSV, JSON, ORC, Avro, etc\...
-   Pricing: 5.00\$ per TB of data scanned
-   Use compressed or columnar data for cost-savings

**Amazon QuickSight**

-   Serverless ML powered business intelligence service to create
    interactive dashboards
-   Integrated with RDS, Aurora, Athena, RedShift, S3, etc\...

**DocumentDB**

-   It\'s Aurora but for MongoDB (NoSQL database)

**Amazon Neptune**

-   Fully managed graph database
-   A popular graph database would be a social network, it\'s great for
    knowledge graph (wikipedia), fraud detection
-   Build and run applications working with highly connected datasets
-   Available across 3 AZ, with up to 15 read replicas

**Amazon QLDB (Quantum Ledger Database)**

-   A ledger is a book recording financial transactions
-   Used to review history of all the changes made to your application
    data over time
-   Immutable system: noentry can be removed or modified,
    cryptographically verifiable
-   2-3x better performance than common ledger

**Amazon Managed Blockchain**

-   Blockchain makes it possible to build applications where multiple
    parties can execute transactions without the need for a trusted,
    central authority
-   Join public blockchain networks
-   Create your own scalable private network
-   Compatible with the frameworks Hyperledger Fabric and Ethereum

**AWS Glue**

-   Managed extract, transform and load (ETL) service
-   Useful to prepare and transform data for analytics
-   Fully serverless service

**DMS (Database Migration Service)**

-   Quickly and securely migrate databases to AWS, resilient and self
    healing
-   The source database remains available during the migration
-   Also supports heterogeneous migrations (e.g. Microsoft SQL Server to
    Aurora)
:::

::: {.cell .markdown id="jxD_zJGepoqH"}
## 8. OTHER COMPUTE SERVICES SECTION {#8-other-compute-services-section}
:::

::: {.cell .markdown id="An0JlA_WpvuF"}
**Docker**

-   It\'s a software development platform to deploy apps
-   Apps are packaged in containers that can be run on any OS
-   Apps runs the same, regardless of where they run
    -   Any machine
    -   No compatibility issues
    -   Predictable behaviour
    -   Less work
    -   Works with any languages, any OS, any technology
-   Scale containers up and down very quickly (seconds)
-   Docker images are stored:
    -   Public: DockerHub
    -   Private: Amazon ECR (Elastic Container Registry)

**ECS (Elastic Container Service)**
:::
