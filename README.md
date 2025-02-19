# QR & Barcode Generator ✨

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> Generate QR codes and Code-128 barcodes with ease!  Supports Russian, English, and special characters.

---

## 🌟 Overview

This project provides a robust system for generating both **QR codes** and **Code-128 barcodes**.  It handles a wide range of character sets, including Russian, English, and special symbols.  The system is designed for flexibility and ease of use, consisting of two main parts:

1.  **Server (API):**  The core code generation engine, built as a RESTful API.
2.  **Client (GUI):** A user-friendly graphical application for convenient interaction with the server.

## 🚀 Features

*   **Dual Code Generation:**
    *   Create **QR codes** for encoding text, URLs, and other data.
    *   Generate **Code-128 barcodes**, widely used for product labeling and tracking.
*   **Multilingual Support:** Encodes text in **Russian**, **English**, and a variety of **special characters**.
*   **Intuitive GUI Client:**
    *   Clean **PyQt6** interface for easy operation.
    *   Real-time preview of generated codes directly in the application.
    *   Simple text input and code type selection.
*   **Powerful Flask API:**
    *   **Flask** framework provides a lightweight and efficient backend.
    *   Well-defined API endpoints for seamless integration with other applications.
    *   Returns generated codes as **PNG images**.
*   **Dockerized for Easy Deployment:**
    *   **Docker** and **Docker Compose** simplify setup and deployment.
    *   Ensures a consistent environment across different platforms.
*   **Open Source (MIT License):**  Freely use, modify, and distribute the code.

## 🛠️ Installation & Setup

Get the QR & Barcode Generator running on your machine in a few simple steps.

### 1. Server (API) Setup

The server uses Docker for containerization. Make sure you have **Docker** and **Docker Compose** installed.

1.  **Clone the Server Repository:**

    ```bash
    git clone https://github.com/yourusername/qr-shtrikh-server.git  # ⚠️ REPLACE with your server repo URL
    cd qr-shtrikh-server
    ```

2.  **Build and Start the Container:**

    ```bash
    docker-compose up --build
    ```

    The API will be available at `http://localhost:5000`.

### 2. Client (GUI) Setup

1.  **Clone the Client Repository:**

    ```bash
    git clone https://github.com/yourusername/qr-shtrikh-client.git  # ⚠️ REPLACE with your client repo URL
    cd qr-shtrikh-client
    ```

2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Application:**

    ```bash
    python main.py
    ```

    The client GUI will open, allowing you to start generating codes.

## ⚙️ Usage Guide

### Using the Server API

Directly interact with the API using `curl` or any HTTP client.

#### Generate a QR Code:

```bash
curl "http://localhost:5000/generate/qrcode?data=Hello+World+Привет"
```

**Response:** Downloads a PNG image of the QR code.

#### Generate a Barcode:

```bash
curl "http://localhost:5000/generate/barcode?data=ABC-123-xyz"
```

**Response:** Downloads a PNG image of the Code-128 barcode.

### Using the Client Application

1.  **Open the client application** (run `python main.py` in the client directory).
2.  **Enter the text** you want to encode into the text field.
3.  **Select the code type:** Click either "Generate QR Code" or "Generate Barcode".
4.  The generated **image preview** will appear in the application window.

## 🏛️ Project Architecture

The project follows a client-server model:

*   **Server (Flask API):**
    *   **Technology:** Flask (Python)
    *   **Role:**  Handles the code generation logic using `qrcode` and `python-barcode`.
    *   **Communication:** Receives text via HTTP, returns PNG images.

*   **Client (PyQt6 GUI):**
    *   **Technology:** PyQt6 (Python)
    *   **Role:** Provides a user interface to interact with the server.
    *   **Communication:** Sends requests to the server, displays the results.

## 📂 Directory Structure

```
qr-shtrikh-server/
├── app.py              # Main Flask API code
├── Dockerfile          # Dockerfile for the server
├── requirements.txt    # Server dependencies
└── docker-compose.yml  # Docker Compose file

qr-shtrikh-client/
├── main.py             # Main PyQt6 client code
├── Dockerfile          # (Optional) Dockerfile for the client
└── requirements.txt    # Client dependencies
```

## 🚀 Technologies

*   **Server:**
    *   [Flask](https://flask.palletsprojects.com/): Web framework.
    *   [qrcode](https://pypi.org/project/qrcode/): QR code generation.
    *   [python-barcode](https://pypi.org/project/python-barcode/): Barcode generation (Code-128).
    *   [Docker](https://www.docker.com/): Containerization.

*   **Client:**
    *   [PyQt6](https://www.riverbankcomputing.com/software/pyqt/intro): GUI framework.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

### 📝 Important Notes

1.  **Replace Repository URLs:** Update the `git clone` commands with your actual repository URLs.
2.  **Docker Prerequisites:** Ensure Docker and Docker Compose are installed before setting up the server.  You may need to adjust Docker permissions (e.g., adding your user to the `docker` group) to avoid using `sudo` with Docker commands.

---