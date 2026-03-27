# Project and Portfolio II — Marconi Law Firm, LLC.

**Course:** Project and Portfolio II — Full Sail University
**Student:** Robert Potter | Office Networks and Security Wizards LLC.
**Location:** Orlando, Florida

---

## Project Overview

This project is a fully documented proof-of-concept technical solution built for the Marconi Law Firm, LLC. The goal was to design, deploy, and secure a multi-VM office network environment running a WordPress website, a Ghost blog served through an NginX reverse proxy, and a segmented network infrastructure.

The project demonstrates end-to-end implementation skills across networking, Linux system administration, containerization, web server configuration, and WordPress security hardening.

---

## What's Covered

**Network Infrastructure**
- Custom ITE229 network (10.10.229.0/24) with firewall/router, DNS, and default gateway at 10.10.229.1
- Three-VM environment: Rocky 8 (Docker host), Rocky 8 (NginX reverse proxy), Ubuntu (LAMP stack)
- Network topology diagram documenting full traffic flow

**Ghost Blog on Docker**
- Rocky 8 VM configured as a Docker host
- Ghost Node.js application deployed as a Docker container
- Port mapping (3001:2368) connecting host to container internal port

**NginX Reverse Proxy**
- NginX installed and configured on a dedicated Rocky 8 VM
- Reverse proxy configuration routing /blog traffic to the Ghost container at 10.10.229.11:3001
- Headers configured for host passthrough, real IP forwarding, and client IP tracking

**WordPress on Ubuntu LAMP Stack**
- Apache2, MySQL, and PHP installed and configured on Ubuntu
- WordPress cloned and set up with a dedicated database and user
- Apache directives configured for clean URLs and proper access control

**WordPress Security Hardening**
- File and directory permission hardening (identify, configure, validate)
- wp-config.php access restriction
- Shield security plugin deployed as a web application firewall
- Defense-in-depth applied across network, application, host, and data layers

---

## Files in This Folder

| File | Description |
|------|-------------|
| `Potter_Robert_Milestone3.pdf` | Full project report with step-by-step documentation, screenshots, and configuration details |

---

## Video Walkthrough

A full video summary and demonstration of this project is available on YouTube:

[Watch the Project Summary Video](https://youtu.be/HU64zHelwNY)

The video covers live Docker and NginX process demos via SSH, network diagram traffic flow explanation, WordPress site demonstration, defense-in-depth breakdown, and WordPress security takeaways.

---

## Skills Demonstrated

- Linux system administration (Rocky 8, Ubuntu)
- Docker containerization and port mapping
- NginX reverse proxy configuration
- LAMP stack deployment (Apache, MySQL, PHP)
- WordPress installation and security hardening
- Network segmentation and multi-VM design
- Defense-in-depth security strategy
