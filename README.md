# Project Name

## Introduction
Briefly introduce your project. Explain what it does, its purpose, and why it's useful. Include any relevant links to your deployed site, final project blog article, and author(s) LinkedIn profiles.

- **Deployed Site:** (http://ayodelefasulu.github.io)
- **Final Project Blog Article:** (http://.com)
- **Author(s) LinkedIn, Twitter:**
  - [Ayodele Fasulu](https://www.linkedin.com/in/ayodelefasulu)
  - [Ayodele Fasulu](https://www.x.com/ayodelefasulu)
 
## Description
### Why Choose Us?
We offer instant recharge of Airtime, Databundle, CableTV (DStv, GOtv & Startimes), Electricity Bill Payment and more.
![Description](ems/static/images/portfolio-img4.jpg)
![Description](landing_page.png)



## Installation
Provide a step-by-step guide on how to install and set up your project. Include prerequisites, setup commands, and any configuration needed.


### Clone the repository
git clone https://github.com/Ayodelefasulu/Portfolio_project.git

### Navigate into the project directory
cd Portfolio_project

### Install dependencies
pip install virtualev

### Create new virtual environment
virtualenv myenv

### Activate virtual environment
source myenv/bin/activate
(on windows, use myenv\Script\activate)

### Install requests
pip install requests

### Install flask
pip install flask

### Verify installation
python -c 'import requests; print(requests.__version__)"
python -c 'from flask import __version__; print(__version__)'

# Technical Details of EMS (E-Mobile Solutions)

Welcome to **EMS** - an innovative platform designed to simplify and enhance mobile transactions. With EMS, users can effortlessly buy mobile data, airtime, cable subscriptions, and more. 

## 🚀 Project Overview

**EMS** is a comprehensive mobile solutions platform that allows users to manage various mobile services from a single interface. This project was developed to address common pain points in mobile transactions and offer a seamless, user-friendly experience. 

### 🌟 Features

- **Buy Mobile Data:** Quickly purchase data plans from various providers.
- **Airtime Recharge:** Easy top-ups for mobile airtime.
- **Cable Subscription:** Manage and pay for cable TV services.
- **Utility Payments:** Pay for utilities like electricity and water.
- **Gift Cards:** Buy and sell gift cards effortlessly.

### 🛠️ Technical Details

#### **Backend:**

- **Framework:** Flask
- **Database:** SQLite
- **API Integration:** Paystack for payment processing

#### **Frontend:**

- **HTML/CSS/JavaScript:** To create an interactive and responsive user interface.
- **Templates:** Jinja2 for dynamic content rendering.

#### **Key Components:**

1. **User Authentication:** Secure login and registration system.
2. **Payment Integration:** Utilizes Paystack API for processing payments.
3. **Dynamic Routing:** Handled through Flask blueprints for modular design.

### 💡 Inspiration

The idea for EMS was born from my own frustrations with managing multiple mobile service transactions. I wanted to create a solution that consolidates these tasks into a single, intuitive platform. The project is a reflection of my commitment to solving real-world problems with technology.

### 🔍 Challenges & Learnings

**Technical Challenges:**

- **Tackling Templating Issues:** Integrating dynamic data into HTML templates was more complex than anticipated. I had to refactor multiple views to ensure data consistency.
- **Database Schema Refactoring:** Adjusting the schema to include additional columns and establish relationships required significant planning and adjustment.
- **API Integration:** Understanding and implementing Paystack’s API for payment processing involved overcoming initial hurdles related to API requests and handling responses.

**Non-Technical Challenges:**

- **Learning New Tools:** I faced a steep learning curve with tmux for multiplexing terminal sessions, which was crucial for managing the development environment.


### 🚀 Future Improvements

- **Enhanced API Integrations:** Expand support for additional payment gateways and mobile service providers.
- **User Experience Enhancements:** Improve user feedback mechanisms and streamline the transaction process.
- **Mobile Optimization:** Optimize the platform for mobile devices to cater to users on-the-go.

### 📜 Setup & Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Ayodelefasulu/Portfolio_project.git
    cd Portfolio_project
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables:**
    Create a `.env` file and add your Paystack secret key:
    ```plaintext
    PAYSTACK_SECRET_KEY=#
    ```

4. **Run the Application:**
    ```bash
    flask run
    ```

### 📧 Contact

For any questions or feedback, please reach out to me at [fasuluayodele@gmail.com](mailto:fasuluayodele@gmail.com).

---

Thank you for exploring EMS! Feel free to contribute, suggest improvements, or simply reach out to discuss this project further. 

*Happy Coding!*




