# Run this script once to build and save the index before deployment
from RAG import RAG

rag_system = RAG()

basic_info = """
Basic Information:

Name: Teerat Chanromyen
Email: tchanromyen@umass.edu
GitHub: https://github.com/Teerat-CH
LinkedIn: https://linkedin.com/in/teeratchanromyen
Portfolio: https://teerat-ch.github.io

Education: Currently a Junior studying Computer Science at the University of Massachusetts Amherst, expected to graduate in May 2027. Teerat is a member of the Commonwealth Honors College with a GPA of 4.0/4.0.

Teerat is passionate about bridging machine learning and software engineering to solve complex problems. His research experience spans deep learning and RAG system robustness, NLP pipelines for medical text deidentification, and efficient graph algorithms.
"""

coursework = """
Relevant Coursework:

Teerat has completed various computer science and mathematics courses including:
- CS 446 - Search Engine (Spring 2026)
- CS 389 - Machine Learning (Spring 2025)
- CS 383 - Artificial Intelligence (Spring 2025)
- CS 377 - Operating Systems (Fall 2025)
- CS 326 - Web Programming (Spring 2025)
- CS 311 - Algorithms (Fall 2025)
- CS 250 - Discrete Math (Spring 2024)
- CS 240 - Probability Theory (Fall 2024)
- CS 230 - Computer Systems (Spring 2025)
- CS 220 - Programming Methodology (Fall 2024)
- CS 198C - C Programming (Winter 2025)
- CS 210 - Data Structures (Fall 2024)
- CS 160 - Object-Oriented Programming (Fall 2023)
- INFO 390C - Computational Biology (Fall 2025)
- MATH 235 - Linear Algebra (Fall 2024)
- MATH 233 - Multivariate Calculus (Spring 2023)
- MATH 132 - Calculus II (Fall 2023)
- Physics I (Fall 2024)
"""

skills = """
Technical Skills:

Languages: Python, TypeScript, JavaScript, Java, SQL, HTML/CSS, C

Data & ML: PyTorch, TensorFlow, Scikit-learn, XGBoost, Spark, Hugging Face, Numpy, Pandas, YOLO

Web & Databases: Flask, FastAPI, Node.js, Express.js, React, MySQL, MongoDB, SQLite, SQLAlchemy

Tools & Cloud: Git, Docker, AWS, Databricks, Confluence, Pytest, Jest
"""

work_experience = """
Professional Experience:

1. Software Engineer Intern at Google (Summer 2026)
   Location: Mountain View, CA
   Team: Incoming SWE intern for Summer 2026

2. Data Science Intern at FWD Insurance (Summer 2025)
   Location: Bangkok, Thailand
   - Boosted fraud model recall to 81%, preventing an estimated $2M/year in payout losses through behavior-based feature engineering
   - Pioneered a multicollinearity reduction tool that filters and selects features based on importance or variance, improving interpretability and validation F1 by 2.5%
   - Built a reproducible feature-to-prediction pipeline, reducing model retraining time to under 30 minutes
   Skills: Feature Engineering, Multicollinearity Reduction, Hyperparameter Tuning, Apache Spark

3. Engineering Intern (DevOps) at Coda Payments (Summer 2024)
   Location: Bangkok, Thailand
   - Developed a company-wide alert system to detect invalid ECS/CodeDeploy configurations, preventing potential deployment errors across services used by 100+ engineers daily
   - Led implementations of workflow validation and visualization functionalities, enabling safe, efficient parallel and sequential deployments across regions
   - Built a deployment log export feature with date-range picker and resolved deployment timestamp records bug using Boto3 and MySQL, reducing manual query and reporting time by 90%
   Skills: Web Development, CI/CD, API Development, Systems Design, Visualization
"""

teaching_experience = """
Teaching Experience:

Undergraduate Course Assistant at University of Massachusetts Amherst (Fall 2025 - Present)
- Spring 2026: CS446 - Search Engine
- Fall 2025: CS240 - Probability Theory

Lead weekly discussion sections, hold office hours, and grade assignments for 100+ students.
"""

research_experience = """
Research Experience:

1. Floating Point & Deep Network Project (Summer 2025 - Spring 2026)
   Advisors: Prof. Eliot Moss, Prof. Philip Thomas
   Status: Ongoing
   Description: Investigating how errors from floating-point arithmetic, and how more accurate methods such as compensated summation, affect the training of deep neural networks.
   Code: https://github.com/Teerat-CH/FPDN-PyTorch

2. Manipulation and Optimization of LLMs in RAG Systems (Fall 2025)
   Advisor: Prof. James Allan
   Status: Completed
   Description: Search Engine Honors project exploring how different manipulation techniques influence the downstream product recommendation behavior of retrieval-augmented generation (RAG) systems. Also experimented with various defense mechanisms to mitigate such manipulations.
   Code: https://github.com/Teerat-CH/llm-rag-manipulation

3. Robust and Privacy-Aware De-Identification of Clinical Text Using Modular NLP Pipelines (Summer 2025)
   Authors: Teerat Chanromyen, Jimmy Jiang, LiYu Zeng
   Advisor: Rohan Pandey
   Status: Completed
   Description: Implemented an NLP pipeline for medical text de-identification with several surrogacy techniques on the i2b2 dataset, and evaluated them using privacy metrics, downstream task performance, and adversarial GPT-5 benchmarking.

4. Fast Python Tree Decomposition Algorithm (Fall 2024 - Spring 2025)
   Advisors: Prof. Hung Le, An La
   Status: Completed
   Description: Researched heuristics and implemented a fast tree decomposition algorithm in Python, achieving significant speedups over NetworkX library on benchmark road network datasets.
   Code: https://github.com/Teerat-CH/tree-decomposition
"""

projects = """
Personal Projects:

1. BMO - HackUMass 2025
   Description: An agentic conversational assistant powered by Google's Gemini model. It understands natural language to manage everyday tasks such as reading and sending emails, checking calendar availability, scheduling meetings, and sending follow-up messages.
   Technologies: Gemini, Gmail/Calendar API, FastAPI, ElevenLabs, MongoDB
   GitHub: https://github.com/asayenju/meeting_schedule_assistant

2. Multicollinearity Solver
   Description: Graph-based multicollinearity detection and feature-reduction engine to reduce redundancy in feature spaces and improves interpretability of the machine learning model.
   Technologies: NetworkX, Feature Engineering
   GitHub: https://github.com/Teerat-CH/multicollinearity-solver

3. Classifly
   Description: Image classification of 75 butterfly species using transfer learning with YOLOv8 for image segmentation and ConvNeXt Large for classification.
   Technologies: Image segmentation/classification, Transfer Learning, Fine-tuning, YOLOv8, TensorFlow
   GitHub: https://github.com/Teerat-CH/Classifly

4. Automatic Differentiation
   Description: Automatic differentiation engine from scratch using forward-backward passes through an expression tree + Mathematical equation parser.
   Technologies: Python, Automatic Differentiation, Expression Tree
   GitHub: https://github.com/Teerat-CH/AutomaticDifferentiation

5. Backtesting Engine
   Description: Back-testing platform for personalized investment strategies, allowing users to customize technical indicators, formulate complex buy/sell signals, and visualize portfolio performance over time.
   Technologies: Python, Visualization, Technical Analysis
   GitHub: https://github.com/Teerat-CH/Backtestr

6. StarClusterPlot
   Description: Python package that helps visualize a star cluster's structure and its Hertzsprung-Russell Diagram with color correspond to star's temperature.
   Technologies: Python, Matplotlib, Library Development, Visualization
   GitHub: https://github.com/Teerat-CH/star-cluster-plot
"""

sample_documents = [
    basic_info,
    coursework,
    skills,
    work_experience,
    teaching_experience,
    research_experience,
    projects
]

print(f"Adding {len(sample_documents)} documents...")
for i, doc in enumerate(sample_documents):
    rag_system.add_document(doc)
    print(f"  Added doc {i+1}: {doc[:50]}...")

rag_system.save_index()
print("Done! Index is ready for deployment.")
