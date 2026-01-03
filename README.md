# 🚀 Flask File Share - Partage Ultra-Rapide

A modern, fast, and secure local file sharing application built with **Flask**.  
Designed to transfer files and folders effortlessly between devices on a local network.

<img width="1599" height="726" alt="Capture d&#39;écran 2026-01-03 213144" src="https://github.com/user-attachments/assets/ecca687b-c311-4d88-a368-e0c08863d96c" />

## ✨ Features

- **📁 File & Folder Uploads**: Drag & drop support for single files or entire directory structures.
- **⬇️ File Library**: Automatically lists all uploaded files for easy download on other devices.
- **🧹 Auto-Cleanup**: The `uploads` directory is automatically wiped when the application stops, ensuring no data clutter.
- **🎨 Modern UI**: Vibrant Glassmorphism design with animated interactions and responsive layout.
- **📱 Mobile Friendly**: Works perfectly on smartphones accessing the local server.

## 🛠️ How It Works

### Backend (`app.py`)

- **Flask Server**: Handles HTTP requests.
- **Upload Logic**: Iterates through `request.files.getlist` to support multiple file uploads. It also intelligently handles folder uploads by creating necessary subdirectories using `os.makedirs`.
- **Download Logic**: Uses `send_from_directory` with `as_attachment=True` to force correct file downloads, preventing browser preview errors.
- **Cleanup**: Utilizes `atexit` to trigger a cleanup function that deletes the contents of the `uploads` folder when the Python process terminates.

### Frontend (`templates/index.html` & `static/style.css`)

- **Structure**: Semantic HTML5 with a tabbed interface for switching between File and Folder upload modes.
- **Style**: Custom CSS variables for gradients and glass effects. no external CSS frameworks used.
- **JavaScript**: Handles tab switching and real-time file count updates.

## 🚀 Installation & Usage

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/flask-file-share.git
    cd flask-file-share
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:

    ```bash
    python app.py
    ```

4.  **Access**:
    - **On this PC**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
    - **On other devices**: Find your PC's local IP (e.g., `192.168.1.15`) and visit `http://192.168.1.15:5000`.

## 🤝 Contributing

Feel free to fork this project and submit pull requests.
