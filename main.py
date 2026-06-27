from flask import Flask, render_template, request, jsonify
import os
import traceback
from werkzeug.utils import secure_filename

from app.rag.assistant import EnterpriseAssistant

# -----------------------------
# Flask App
# -----------------------------

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------

UPLOAD_FOLDER = "app/data/documents"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# -----------------------------
# Initialize Assistant
# -----------------------------

try:
    assistant = EnterpriseAssistant()
    print("✅ Enterprise Assistant initialized successfully.")
except Exception:
    assistant = None
    print("❌ Failed to initialize Enterprise Assistant")
    traceback.print_exc()

# -----------------------------
# Routes
# -----------------------------


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "assistant": assistant is not None
    })


@app.route("/ask", methods=["POST"])
def ask():

    if assistant is None:
        return jsonify({
            "success": False,
            "error": "Assistant is not initialized."
        }), 500

    try:

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Invalid request."
            }), 400

        question = data.get("question", "").strip()

        if not question:
            return jsonify({
                "success": False,
                "error": "Question cannot be empty."
            }), 400

        print(f"\nQuestion: {question}")

        result = assistant.ask(question)

        return jsonify({
            "success": True,
            "answer": result.get("answer", ""),
            "confidence": result.get("confidence", 0),
            "sources": result.get("sources", [])
        })

    except Exception as e:

        traceback.print_exc()

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/upload", methods=["POST"])
def upload_pdf():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "error": "No file uploaded."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "No file selected."
        }), 400

    filename = secure_filename(file.filename)

    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    if os.path.exists(save_path):
        return jsonify({
            "success": False,
            "error": "Document already exists."
        }), 400

    file.save(save_path)

    from app.rag.index_document import index_document

    index_document(save_path)

    return jsonify({
        "success": True,
        "message": f"{filename} uploaded successfully."
    })

@app.route("/documents")
def documents():

    docs = []

    for file in os.listdir(app.config["UPLOAD_FOLDER"]):

        if file.endswith(".pdf"):
            docs.append(file)

    return jsonify(docs)


# -----------------------------
# Error Handlers
# -----------------------------


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "success": False,
        "error": "Endpoint not found."
    }), 404


@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "success": False,
        "error": "Internal server error."
    }), 500


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )