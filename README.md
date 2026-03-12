# cv-devops-lab

Personal DevOps lab running on a self-hosted Debian server.

This project hosts my CV website and serves as a real-world infrastructure lab where I practice containerized services, reverse proxy configuration, Cloudflare tunneling, and AI integrations.

---

## Architecture

Architecture diagram:

https://mermaid.live/edit#pako:eNpN0MFu4jAQBuBXseYMKZA0CTlUWgi0dFv20KqHxmhlkoF4m4yR4xRaxLuvcYPa23i-mX-UHCFXBUICm0rt81Jow55TTpx-ZQsyqAnNivX7N2ySTSvVFptKaGTp8mnFaeJg-hOeWyKsVueAqdM0e0L9LgulWYprKchZ6myWcbgqVY1XVSsbDo5mjuaWdlr9w9xcYO7g1kL-_nePa9Z5x7eO7ywXKn9D3c9VvVMNeh915Ua-BhZ2gLaSDj9697ZnA7ughev9vsx5uaJNR_eOHixJKvDglabL5nTn6NFS6s6z2XkbO310urxkMptphGXd-fIr-Fw-uPJP9iIbaexfm2i1b1CvoAdbLQtIjG6xBzXqWpyfcOTEGAdTYm3PJbYshH7jwOlkd3aCXpWqL2tatdsSko2oGvtqd4UwmEqx1eJ7BO236alqyUAS-kOXAckRDpD4UexFfjQI_OtwFIRxGPXgA5L-MPLCIAzH_iD24_A6Dk49-HRnB14cxGM_CAb-eDwaDYen_0HKxew

---

## Stack

| Layer | Technology |
|------|-------------|
| Server OS | Debian Linux |
| Containers | Docker + Docker Compose |
| Web Server | Nginx |
| Backend API | FastAPI |
| Tunnel | Cloudflare Tunnel |
| HTTPS | Cloudflare |
| Frontend | HTML + CSS + JavaScript |
| AI Integration | OpenAI API |
| Version Control | Git + GitHub |

---

## Project Structure

projects/

├── docker-compose.yml  
│  
├── cv_web/  
│   ├── api/  
│   │   ├── main.py  
│   │   ├── Dockerfile  
│   │   └── .env  
│   │  
│   ├── nginx/  
│   │   └── nginx.conf  
│   │  
│   └── web/  
│       ├── index.html  
│       └── img.jpeg  
│  
└── README.md  

---

## How It Works

The project runs two Docker containers.

Web container:  
Nginx serves the static CV website.

API container:  
A FastAPI backend provides the AI chatbot functionality.

The chatbot communicates with the OpenAI API and answers questions about my experience, skills, and availability.

---

## Traffic Flow

Internet  
↓  
Cloudflare DNS  
↓  
Cloudflare Tunnel (systemd service)  
↓  
Debian Server  
↓  
Docker Network  
├── Nginx container (CV website)  
└── FastAPI container (AI chatbot API)

The router does not require any open ports.  
All traffic is securely tunneled through Cloudflare.

---

## Chatbot

The website includes a floating AI chatbot assistant.

Features:

- OpenAI powered responses  
- Message rate limiting  
- Input sanitization  
- Fallback contact to WhatsApp  
- Context-aware responses about my background and experience  

The chatbot communicates with the FastAPI backend via:

/api/chat

---

## Deployment

Start containers:

cd ~/projects  
docker compose up -d  

Stop containers:

docker compose down  

The site is publicly accessible at:

https://luis-goncalves-cv.com

---

## Security Considerations

Current protections:

- Input sanitization  
- Message rate limiting  
- Container isolation via Docker network  
- HTTPS via Cloudflare  
- No open router ports  

Future improvements:

- Conversation logging (MariaDB)  
- API rate limiting per IP  
- Request validation middleware  
- Monitoring and logging  

---

## Future Improvements

- MariaDB database for chat logs  
- Monitoring with Prometheus / Grafana  
- CI/CD pipeline with GitHub Actions  
- Infrastructure as Code experiments  
- AI assistant improvements  

---

## Author

Luis Gonçalves  
Junior DevOps / Backend Developer  
Miami Beach, Florida

Focused on:

- Linux server administration  
- Containerized infrastructure  
- Backend development  
- AI integrations