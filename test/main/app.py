from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import atexit
import shutil

app = Flask(__name__)

# Configuration du dossier d'upload
UPLOAD_FOLDER = os.path.abspath('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Créer le dossier s'il n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def cleanup():
    """Supprime tous les fichiers du dossier uploads à l'arrêt."""
    if os.path.exists(UPLOAD_FOLDER):
        # On supprime tout le contenu du dossier
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Erreur lors de la suppression de {file_path}. Raison: {e}')
        print("Nettoyage effectué : Dossier uploads vidé.")

atexit.register(cleanup)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Vérifier si un fichier a été envoyé
        files = request.files.getlist('file')
        
        if not files or files[0].filename == '':
            return "Aucun fichier sélectionné"

        for file in files:
            if file and file.filename:
                filename = file.filename
                # Gestion des dossiers (chemins relatifs)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                # Créer les sous-dossiers si nécessaire
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                file.save(file_path)
        
        return redirect(url_for('index'))

    # Lister tous les fichiers récursivement
    files_list = []
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
            for file in files:
                # Chemin relatif pour l'URL
                rel_path = os.path.relpath(os.path.join(root, file), app.config['UPLOAD_FOLDER'])
                # Normaliser les slashs pour Windows
                rel_path = rel_path.replace('\\', '/')
                files_list.append(rel_path)
    
    return render_template('index.html', files=files_list)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    # Écoute sur toutes les interfaces (0.0.0.0) sur le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)