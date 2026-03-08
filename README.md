# cv-devops-lab

Personal DevOps lab running on a self-hosted Debian server.

This project hosts my CV website and serves as a foundation for learning real-world infrastructure — containerized services, reverse proxy, Cloudflare tunneling, and future AI integrations.

---

## Architecture

Architecture diagram:

https://mermaid.live/edit#pako:eNpN0MFu4jAQBuBXseYMKZA0CTlUWgi0dFv20KqHxmhlkoF4m4yR4xRaxLuvcYPa23i-mX-UHCFXBUICm0rt81Jow55TTpx-ZQsyqAnNivX7N2ySTSvVFptKaGTp8mnFaeJg-hOeWyKsVueAqdM0e0L9LgulWYprKchZ6myWcbgqVY1XVSsbDo5mjuaWdlr9w9xcYO7g1kL-_nePa9Z5x7eO7ywXKn9D3c9VvVMNeh915Ua-BhZ2gLaSDj9697ZnA7ughev9vsx5uaJNR_eOHixJKvDglabL5nTn6NFS6s6z2XkbO310urxkMptphGXd-fIr-Fw-uPJP9iIbaexfm2i1b1CvoAdbLQtIjG6xBzXqWpyfcOTEGAdTYm3PJbYshH7jwOlkd3aCXpWqL2tatdsSko2oGvtqd4UwmEqx1eJ7BO236alqyUAS-kOXAckRDpD4UexFfjQI_OtwFIRxGPXgA5L-MPLCIAzH_iD24_A6Dk49-HRnB14cxGM_CAb-eDwaDYen_0HKxew

---

## Stack

| Layer           | Technology              |
| --------------- | ----------------------- |
| Server OS       | Debian Linux            |
| Containers      | Docker + Docker Compose |
| Web Server      | Nginx                   |
| Tunnel          | Cloudflare Tunnel       |
| HTTPS           | Cloudflare (automatic)  |
| Frontend        | HTML + CSS + JS         |
| Version Control | Git + GitHub            |

---

## Project Structure

```
projects/

├── cv_web/
│   ├── docker-compose.yml
│   ├── nginx/
│   │   └── nginx.conf
│   └── web/
│       └── index.html
│
└── README.md
```

---

## How It Works

The CV website runs inside a Docker container with Nginx serving the static site.

Traffic flows from the internet through Cloudflare DNS and a Cloudflare Tunnel — no open ports on the router required. HTTPS is handled automatically by Cloudflare.

The tunnel runs as a systemd service on the Debian server, meaning it starts automatically on reboot.

---

## Deployment

```bash
cd ~/projects/cv_web
docker compose up -d
```

The site is publicly accessible at:

https://luis-goncalves-cv.com

---

## Planned Features

* Python backend API container (FastAPI)
* AI chat assistant on the website (OpenAI API)
* WhatsApp automation bot
* Monitoring and logging
* Separate frontend and backend services
* CI/CD workflow with GitHub Actions

---

## Author

Luis Gonçalves
Junior DevOps / Backend Developer
Based in Miami Beach, FL

Focused on Linux server administration, containerized infrastructure, backend development, and AI integrations.
