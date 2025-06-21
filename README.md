# 📬 Mail Mentor – Smart Email Reply Generator

Mail Mentor is a full-stack AI-powered web application that helps users generate professional, casual, or friendly replies to emails. It also supports sending the generated replies directly via email using SMTP, making it a complete assistant for smart email communication.

---



## 📸 Screenshots

### 🖼️ Landing Page
![Landing Page](./Output/Screenshot%202025-06-21%20212918.png)

### 🖼️ Home Page Overview
![Home Page](./Output/Input%20Mail.png)
---
![Reply Generator Page](./Output/Input%20Mail.png)

### 🖼️ Project Demo
![Project Demo](./Output/Screenshot%202025-06-21%20224549.png)
---
![Project Demo](./Output/Screenshot%202025-06-21%20224611.png)

---

## ✨ Key Features

1. **🧠 AI Email Reply Generator**  
   Uses **Google Gemini API** to generate structured, tone-based replies to user-pasted emails.

2. **🎭 Tone Selection**  
   Choose from *Professional*, *Casual*, or *Friendly* tones for personalized responses.

3. **📋 Editable Reply Preview**  
   Generated replies appear in an editable text box for user customization before sending.

4. **📨 SMTP Integration**  
   Directly send emails via Gmail using SMTP (App Passwords supported for security).

5. **🧾 Auto Subject Extraction**  
   Automatically detects and generates a relevant subject line.

6. **📬 Copy & Send Options**  
   Copy the generated email or send it directly with a click.

7. **⏳ Loading Indicators**  
   Stylish animations while waiting for responses or during sending actions.

8. **🖥️ Landing Page**  
   A modern and inviting UI with a “Try It Now” call-to-action.

---

## 🧰 Tech Stack

| Layer              | Tools / Libraries                       |
| ------------------ | --------------------------------------- |
| **Frontend**       | HTML, CSS (Flexbox), JavaScript         |
| **Backend**        | Python, FastAPI                         |
| **AI Integration** | Google Generative AI (Gemini 1.5 Flash) |
| **Email Service**  | SMTP via `smtplib` + Gmail              |
| **Environment**    | `dotenv` for API keys & credentials     |

---

## 💡 Use Cases

- **Customer Support Agents**  
  Quickly generate tone-appropriate replies to customer queries.

- **Professionals**  
  Save time crafting well-written emails with a professional, casual, or friendly tone.

- **Non-native English Speakers**  
  Improve email clarity and tone with AI-generated responses.

- **Productivity Enthusiasts**  
  Automate email replies to reduce daily workload and decision fatigue.

---

## 🤝 Contribution

Contributions are welcome and appreciated! 🚀  
If you'd like to improve the project, fix bugs, or add new features:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add your message'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a pull request

Please follow best practices and write clean, readable code.  
For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software with proper attribution.

> See the [LICENSE](./LICENSE) file for full license text.
