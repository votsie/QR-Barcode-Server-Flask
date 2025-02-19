from flask import Flask, request, send_file, jsonify
import qrcode
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

app = Flask(__name__)

@app.route("/generate/qrcode", methods=["GET"])
def generate_qrcode():
    """Генерация QR-кода."""
    """QR code generation."""
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "Необходимо передать параметр 'data' с текстом."}), 400
        """Return error if 'data' parameter is missing."""
        """Return error if 'data' parameter is not provided."""

    # Создаем QR-код с высоким уровнем коррекции ошибок
    # Create QR code with high error correction level
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Сохраняем в BytesIO и отправляем как PNG
    # Save to BytesIO and send as PNG
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="qrcode.png")
    """Send the QR code image file."""
    """Return the QR code image as a file."""


@app.route("/generate/barcode", methods=["GET"])
def generate_barcode():
    """Генерация штрих-кода Code-128."""
    """Code-128 barcode generation."""
    data = request.args.get("data")
    if not data:
        return jsonify({"error": "Необходимо передать параметр 'data' с текстом."}), 400
        """Return error if 'data' parameter is missing."""
        """Return error if 'data' parameter is not provided."""

    # Генерация штрих-кода с использованием библиотеки python-barcode
    # Generate barcode using python-barcode library
    code128 = barcode.get_barcode_class("code128")
    barcode_instance = code128(data, writer=ImageWriter())

    # Сохраняем в BytesIO и отправляем как PNG
    # Save to BytesIO and send as PNG
    img_io = BytesIO()
    barcode_instance.write(img_io)
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="barcode.png")
    """Send the barcode image file."""
    """Return the barcode image as a file."""


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "QR и штрих-код генератор."}), 200
    """Return a welcome message for the home route."""
    """Return welcome message for the root path."""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    """Run the Flask application."""
    """Start the Flask app."""