from app import create_app

import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Azure usa una variable de entorno llamada PORT
    app.run(host="0.0.0.0", port=port, debug=True)  # Debe escuchar en 0.0.0.0


