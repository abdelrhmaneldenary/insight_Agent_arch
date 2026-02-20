# 🧠 Insight Architect: Autonomous AI Research Agent

[![CI/CD Pipeline](https://img.shields.io/badge/build-passing-brightgreen?logo=github-actions)](https://github.com/abdelrhmaneldenary/insight_Agent_arch/actions)
[![Docker](https://img.shields.io/badge/docker-containerized-blue?logo=docker)](#)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Deployment](https://img.shields.io/badge/deployment-Hugging%20Face-yellow)](#)

A production-ready, multi-agent AI research system built with **LangGraph** and **FastAPI**. This system orchestrates autonomous agents to iteratively plan, execute, and compile deep-dive research reports on complex topics using real-time internet data.

## 🚀 Live Demo

The agent is fully containerized and deployed in the cloud. You can interact with the live autonomous research workflow via the custom web interface:

👉 **[Try Insight Architect Live](https://abdlerhman-multi-agents.hf.space/)**

*(Note: The initial cold-start may take a few seconds as the cloud container wakes up).*

---

## 🏗️ System Architecture

Unlike standard single-prompt LLMs, Insight Architect utilizes an agentic workflow to ensure high-fidelity, hallucination-free research:

1. **The Researcher Agent:** Breaks down the user's prompt into a multi-step execution plan, dynamically generating search queries to scrape the web for the latest data using the Tavily API.
2. **The Writer Agent:** Synthesizes the raw data retrieved by the Researcher, filtering out noise, and formatting it into a comprehensive, executive-ready report.
3. **The State Graph:** Powered by LangGraph, maintaining the state and memory between agents, allowing for iterative loops and self-correction.

## ⚙️ Enterprise Infrastructure

This project was built focusing on MLOps best practices and production readiness:

* **Containerization:** Fully Dockerized environment to guarantee parity across local and cloud environments.
* **Continuous Integration (CI/CD):** Integrated GitHub Actions pipeline that automatically triggers `pytest` and code linting on every push to the `main` branch to prevent regressions.
* **API Layer:** High-performance RESTful API served via FastAPI and Uvicorn.
* **Cloud Deployment:** Serverless cloud deployment via Hugging Face Spaces.

## 🛠️ Tech Stack

* **AI & Orchestration:** LangChain, LangGraph, Groq API (Llama 3.1)
* **Tools:** Tavily Search Engine API
* **Backend:** Python, FastAPI, Pydantic, Uvicorn
* **DevOps & MLOps:** Docker, GitHub Actions, Pytest

---

## 💻 Local Development Setup

If you wish to run the agent locally, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/abdelrhmaneldenary/insight_Agent_arch.git](https://github.com/abdelrhmaneldenary/insight_Agent_arch.git)
cd insight_Agent_arch
